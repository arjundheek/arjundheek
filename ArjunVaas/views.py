import base64
import math
import os
import random
import shutil
from io import BytesIO
from random import randrange

from PIL import Image
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from Accounts.models import *
from django.core.files.images import ImageFile
from django.http.response import JsonResponse
from .serializers import ProductSerializer

selected_profile = Profile()
profile_settings = ProfileSettings()


def get_user_profile(user):
    global selected_profile, profile_settings

    profile_settings = ProfileSettings.objects.get(user=user)
    selected_profile = Profile.objects.get(id=profile_settings.main_profile.id)


def check_active_profile(request):
    global profile_settings

    if profile_settings.active == 0:
        template = loader.get_template('Accounts/account-renewal.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    return True


def index(request):
    template = loader.get_template('ArjunVaas/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def home(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings
    }

    """
    if not selected_profile.picture:
        template = loader.get_template('ArjunVaas/home.html')
    else:
        template = loader.get_template('ArjunVaas/user-profile-edit.html')
    """
    template = loader.get_template('ArjunVaas/home.html')
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def products(request, category):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    selected_colors, selected_types = [], []

    if request.method == 'GET':
        get_colors = request.GET.get('colors')
        get_types = request.GET.get('types')

        if get_colors and get_colors != '[]':
            get_colors = get_colors.replace('"', '')
            get_colors = get_colors.replace("'", '')
            get_colors = get_colors.replace('[', '')
            get_colors = get_colors.replace(']', '')

            if ',' in get_colors:
                for gc in get_colors.split(','):
                    selected_colors.append(gc.replace("'", ""))
            else:
                selected_colors.append(get_colors)

        if get_types and get_types != '[]':
            get_types = get_types.replace('"', '')
            get_types = get_types.replace("'", '')
            get_types = get_types.replace('[', '')
            get_types = get_types.replace(']', '')

            if ',' in get_types:
                for gt in get_types.split(','):
                    selected_types.append(gt.replace("'", ""))
            else:
                selected_types.append(get_types)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    data_products = []

    data_products = Product.objects.all().filter(category=category)
    category_obj = Category.objects.get(id=category)
    brand = Brand.objects.get(id=category_obj.brand.id)

    gender = data_products[0].gender

    display_products = []
    types = []
    colors = []

    if len(data_products) > 0:
        for p in data_products:
            if p.gender.lower() == selected_profile.gender.lower():
                st, sc = True, True
                if len(selected_types) > 0:
                    if p.type not in selected_types:
                        st = False

                if len(selected_colors) > 0:
                    if p.color not in selected_colors:
                        sc = False

                if st and sc:
                    display_products.append(p)

    for dp in display_products:
        if dp.color not in colors:
            colors.append(dp.color)
        if dp.type not in types:
            types.append(dp.type)

    extra_products = []
    if len(display_products) % 2 != 0:
        extra_products.append(1)

    template = loader.get_template('ArjunVaas/products.html')
    context = {
        'category': category,
        'category_name': Category.objects.get(id=category).title,
        'gender': gender,
        'products': display_products,
        'colors': colors,
        'types': types,
        'banner': Banner.objects.filter(page="products")[0],
        'selected_colors': selected_colors,
        'selected_types': selected_types,
        'brand_name': brand.name,
        'extra_products': extra_products,
        'selected_profile': selected_profile,
        'profile_settings': profile_settings,
        'profile_picture': selected_profile.picture
    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def product(request, id):
    global profile_settings, selected_profile
    # get_user_profile(request.user)
    try_on_image = request.GET.get('img', None)
    product = Product.objects.get(id=id)
    category = Category.objects.get(id=product.category.id)
    brand = Brand.objects.get(id=category.brand.id)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    template = loader.get_template('ArjunVaas/product.html')
    select_try_on = {
        'main_image':product.try_on_main_image.url if product.try_on_main_image else '',
        'image1':product.try_on_image1.url if product.try_on_image1 else '',
        'image2':product.try_on_image2.url if product.try_on_image2 else '',
    }
    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings,
        'product': product,
        'category': category,
        'brand': brand,
        'profile_picture': selected_profile.picture,
        'try_on_image': select_try_on.get(try_on_image,product.try_on_main_image),
    }
    return HttpResponse(template.render(context, request))


def ProductJson(request, category):
    global profile_settings, selected_profile
    products = Product.objects.filter(category = category,
                gender__icontains=selected_profile.gender.lower())
    
    serializer = ProductSerializer(products, many=True)

    return JsonResponse({
        'success': True,
        'data':serializer.data,
    })

@login_required(login_url='/login/')
def slider2(request):
    global profile_settings, selected_profile
    get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    template = loader.get_template('ArjunVaas/slider2.html')
    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings
    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def user_info(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    # profiles = Profile.objects.all().filter(user=request.user)
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.gender == '' or profile.picture == '' or profile.age == 0 or profile.height == 0.0:
            profile.active = False
        else:
            profile.active = True

        profile.height = f"{profile.height}".replace('.', "'") + '"'

    template = loader.get_template('ArjunVaas/user-info.html')
    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings,
        'profiles': profiles
    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def user_profile(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    if request.method == 'POST':
        skin = request.POST['colorpicker']
        selected_profile.skin = skin
        selected_profile.save()

    sizes = ['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL']
    adult_heights = {4.0: '4’0”', 4.1: '4’1”', 4.2: '4’2”', 4.3: '4’3”', 4.4: '4’4”', 4.5: '4’5”',
                     4.6: '4’6”', 4.7: '4’7”', 4.8: '4’8”', 4.9: '4’9”', 5.0: '5’0”', 5.1: '5’1”',
                     5.2: '5’2”', 5.3: '5’3”', 5.4: '5’4”', 5.5: '5’5”',
                     5.6: '5’6”', 5.7: '5’7”', 5.8: '5’8”', 5.9: '5’9”', 6.0: '6’0”'}
    baby_height = {3.0: '3’0”', 3.1: '3’1”', 3.2: '3’2”', 3.3: '3’3”', 3.4: '3’4”', 3.5: '3’5”',
                   3.6: '3’6”', 3.7: '3’7”', 3.8: '3’8”', 3.9: '3’9”', 4.0: '4’0”'}

    if 'baby' in selected_profile.gender:
        heights = baby_height
    else:
        heights = adult_heights

    """
    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status
    """

    template = loader.get_template('ArjunVaas/user-profile.html')
    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings,
        'sizes': sizes,
        'heights': heights
    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def create_new_profile(request):
    global profile_settings, selected_profile

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status


    new_user = User()
    new_user.username = random.randint(100000, 999999)
    new_user.password = random.randint(100000, 999999)
    new_user.email = random.randint(100000, 999999)
    new_user.save()
    new_profile = Profile()
    new_profile.user = new_user
    new_profile.save()

    selected_profile = new_profile
    profile_settings.main_profile = new_profile
    profile_settings.user = new_user
    profile_settings.active = True
    profile_settings.save()

    return redirect('home')


# @login_required(login_url='/login/')
def edit_profile(request):
    global profile_settings, selected_profile

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    if request.method == 'POST':
        profile = Profile.objects.get(id=request.POST['edit-profile'])
        selected_profile = profile
        profile_settings.user = profile.user
        profile_settings.main_profile = profile
        profile_settings.active = True
        profile_settings.save()

    return redirect('home')


# @login_required(login_url='/login/')
def delete_profile(request):
    global profile_settings, selected_profile

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    if request.method == 'POST':
        profiles = Profile.objects.all()
        profile = Profile.objects.get(id=request.POST['delete-profile'])

        for p in profiles:
            if p != profile:
                selected_profile = p
                profile_settings.user = p.user
                profile_settings.main_profile = p
                profile_settings.active = 1
                profile_settings.save()
                break

        profile.delete()

    return redirect('user-info')


# @login_required(login_url='/login/')
def update_user_profile(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    if request.method == 'POST':
        selected_profile.size = request.POST['select-body-size']
        selected_profile.height = request.POST['select-body-height']

        selected_profile.save()

    """
    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status
    """
    if profile_settings.active == 1:
        return redirect('user-info')
    else:
        template = loader.get_template('Accounts/account-renewal.html')

    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def renew_profile(request):
    global profile_settings, selected_profile
    get_user_profile(request.user)

    if request.method == 'POST':
        profile_settings.active = 1
        profile_settings.save()

    template = loader.get_template('ArjunVaas/brands.html')
    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings,
        'profile_picture': selected_profile.picture
    }

    return redirect('home')


# @login_required(login_url='/login/')
def user_profile_edit(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    if request.method == 'POST':
        if request.POST['selected_gender'] != selected_profile.gender:
            selected_profile.height = 0.0
            selected_profile.size = ''

        selected_profile.gender = request.POST['selected_gender']
        selected_profile.name = request.POST.get('name', False)
        selected_profile.age = request.POST.get('age', False)
        selected_profile.phone = request.POST.get('phone', False)

        if request.POST['image_url']:
            if selected_profile.picture:
                # Delete previous image
                selected_profile.picture.delete()

            image_name = randrange(1000000, 10000000)

            with open(f'static/uploads/profiles/{image_name}.jpg', 'wb') as fh:
                fh.write(base64.b64decode(request.POST['image_url'].replace('data:image/png;base64,', '')))

            reopen = open(f"static/uploads/profiles/{image_name}.jpg", "rb")
            django_file = File(reopen)

            selected_profile.picture = django_file
            selected_profile.user_id = selected_profile.user.id
            selected_profile.save()
            django_file.close()
            os.remove(f"static/uploads/profiles/{image_name}.jpg")

        #selected_profile.save()
    """
    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status
    """

    template = loader.get_template('ArjunVaas/user-profile-edit.html')
    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings,
        'img_name': ''
    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def category(request, brand):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    template = loader.get_template('ArjunVaas/category.html')

    products = Product.objects.all()
    categories = Category.objects.all().filter(brand=brand)
    brand_obj = Brand.objects.get(id=brand)

    # Check if category has products
    sorted_categories = []
    for c in categories:
        c.active = 0
        for p in products:
            if p.category.id == c.id and p.gender == selected_profile.gender:
                c.active = 1
                sorted_categories.append(c)
                break

    # Sort by active / inactive
    for c in categories:
        c.active = 1
        if c not in sorted_categories:
            c.active = 0
            sorted_categories.append(c)
    selected_colors, selected_types = [], []
    if request.method == 'GET':
        get_colors = request.GET.get('colors')
        get_types = request.GET.get('types')

        if get_colors and get_colors != '[]':
            get_colors = get_colors.replace('"', '')
            get_colors = get_colors.replace("'", '')
            get_colors = get_colors.replace('[', '')
            get_colors = get_colors.replace(']', '')

            if ',' in get_colors:
                for gc in get_colors.split(','):
                    selected_colors.append(gc.replace("'", ""))
            else:
                selected_colors.append(get_colors)

        if get_types and get_types != '[]':
            get_types = get_types.replace('"', '')
            get_types = get_types.replace("'", '')
            get_types = get_types.replace('[', '')
            get_types = get_types.replace(']', '')

            if ',' in get_types:
                for gt in get_types.split(','):
                    selected_types.append(gt.replace("'", ""))
            else:
                selected_types.append(get_types)

    data_products = []
    if len(sorted_categories) > 0:
        data_products = Product.objects.all().filter(category_id=sorted_categories[0].id)
        category_obj = Category.objects.get(id=sorted_categories[0].id)
        brand = Brand.objects.get(id=category_obj.brand.id)

    

    display_products = []
    types = []
    colors = []

    if len(data_products) > 0:
        gender = data_products[0].gender
        for p in data_products:
            if p.gender.lower() == selected_profile.gender.lower():
                st, sc = True, True
                if len(selected_types) > 0:
                    if p.type not in selected_types:
                        st = False
                colors.append(p.color)
                types.append(p.type)

                if len(selected_colors) > 0:
                    if p.color not in selected_colors:
                        sc = False

                if st and sc:
                    display_products.append(p)

    # for dp in display_products:
    #     if dp.color not in colors:
    #         colors.append(dp.color)
    #     if dp.type not in types:
    #         types.append(dp.type)

    extra_products = []
    if len(display_products) % 2 != 0:
        extra_products.append(1)
    print(colors, selected_colors)

    profile_status = check_active_profile(request)
    
    context = {
        'brand_name': brand_obj.name,
        'logo': brand_obj.logo,
        'categories': sorted_categories,
        'banner': Banner.objects.filter(page="categories")[0],
        'selected_profile': selected_profile,
        'profile_settings': profile_settings
    }

    context.update({
        'category': category,
        #'category_name': Category.objects.get(id=38).title,
        'gender': gender,
        'products': display_products,
        'colors': colors,
        'types': types,
        'banner': Banner.objects.filter(page="products")[0],
        'selected_colors': selected_colors,
        'selected_types': selected_types,
        'brand_name': brand.name,
        'extra_products': extra_products,
        'profile_picture': selected_profile.picture
        })
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def brands(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    brands = Brand.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    sorted_brands = []

    for brand in brands:
        for product in products:
            for category in categories:
                if product.gender.lower() == selected_profile.gender:
                    if product.category == category and category.brand == brand:
                        brand.active = True
                        if brand not in sorted_brands:
                            sorted_brands.append(brand)

    # Sort brands
    for b in brands:
        sb_exist = False
        for sb in sorted_brands:
            if sb.id == b.id:
                sb_exist = True
                break

        if not sb_exist:
            sorted_brands.append(b)

    template = loader.get_template('ArjunVaas/brands.html')
    context = {
        'brands': sorted_brands,
        'banner': Banner.objects.filter(page="brand")[0],
        'selected_profile': selected_profile,
        'profile_settings': profile_settings,
        'profile_picture': selected_profile.picture
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def account_renewal(request):
    global profile_settings, selected_profile
    get_user_profile(request.user)

    template = loader.get_template('ArjunVaas/account-renewal.html')
    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings
    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def account_delete(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    template = loader.get_template('ArjunVaas/account-delete.html')
    context = {
        'selected_profile': selected_profile,
        'profile_settings': profile_settings,
        'profile_picture': selected_profile.picture
    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def select_profile(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    if request.method == 'POST':
        id = request.POST['select-profile']
        main_profile = Profile.objects.get(id=id)
        selected_profile = main_profile
        profile_settings.user = main_profile.user
        profile_settings.main_profile = main_profile
        profile_settings.active = True
        profile_settings.save()

    return redirect('brands')


@login_required(login_url='/login/')
def select_photo(request):
    global profile_settings, selected_profile
    get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    if request.method == 'POST':
        id = request.POST['select-photo']
        profile_settings.main_profile = Profile.objects.get(id=id)
        profile_settings.save()

    return redirect('user-profile-edit')


# @login_required(login_url='/login/')
def save_tryon(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    if request.method == 'POST':
        id = request.POST.get('product')
        try_on_image_type = request.POST.get('try_on_image_type')
        product = Product.objects.get(id=id)

        new_tryon = True

        tryons = Tryon.objects.all()
        for t in tryons:
            if t.product == product and t.image == product.main_image:
                new_tryon = False

        if len(tryons) < 10 and new_tryon:
            tryon = Tryon()
            tryon.product = product
            tryon.profile = selected_profile
            if try_on_image_type == 'main_image':
                tryon.image = product.try_on_main_image
            elif try_on_image_type == 'image1':                
                tryon.image = product.try_on_image1
            else:
                tryon.image = product.try_on_image2
            
            tryon.url = product.url
            tryon.save()

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


# @login_required(login_url='/login/')
def tryons(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    tryons = Tryon.objects.all()

    extra_tryons = []
    if len(tryons) % 2 != 0:
        extra_tryons.append(1)

    # profile_status = check_active_profile(request)
    # if isinstance(profile_status, HttpResponse):
    #     return profile_status

    template = loader.get_template('ArjunVaas/tryons.html')
    context = {
        'tryons': tryons,
        'extra_tryons': extra_tryons,
        'banner': Banner.objects.filter(page="tryons")[0],
        'selected_profile': selected_profile,
        'profile_settings': profile_settings,
        'profile_picture': selected_profile.picture
    }
    return HttpResponse(template.render(context, request))


# @login_required(login_url='/login/')
def delete_tryon(request):
    global profile_settings, selected_profile
    # get_user_profile(request.user)

    profile_status = check_active_profile(request)
    if isinstance(profile_status, HttpResponse):
        return profile_status

    if request.method == 'POST':
        tryon = Tryon.objects.get(id=request.POST['tryon'])
        tryon.delete()

    return redirect('tryons')
