from django.shortcuts import render, redirect
from jalali_date import datetime2jalali, date2jalali
from .models import *
from .models import Room
from django.shortcuts import get_object_or_404
from kavenegar import *
import random
from .forms import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from khayyam import JalaliDate


def my_view(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')


def index(request):
    room_suggested = Room.objects.filter(suggested=True)[:5]
    showvip = Contact.objects.filter(show_in_comments_two=True)[:5]
    context = {
        'room_suggested': room_suggested,
        'showvip': showvip
    }
    return render(request, 'index/index.html', context)


def about(request):
    return render(request, 'about/about.html')


def error404(request, exception):
    return render(request, '404/404.html', status=404)


def coming_soon(request):
    return render(request, 'coming-soon/coming-soon.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, phone=phone, message=message, subject=subject)

    return render(request, 'contact/contact.html')


def frequently_questions(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, phone=phone, message=message, subject=subject)

    return render(request, 'frequently-questions/frequently-questions.html')


def privacy_policy(request):
    return render(request, 'privacy-policy/privacy-policy.html')


def room(request):
    rooms = Room.objects.filter(suggested=False)
    room_suggested = Room.objects.filter(suggested=True)
    context = {
        'rooms': rooms,
        'room_suggested': room_suggested
    }

    return render(request, 'room/room.html', context)


def calculate_reserve_day(start_date, finish_date, room_price):
    global total_day, total_price
    start_day = int(start_date.split("/")[2])
    finish_day = int(finish_date.split("/")[2])
    start_month = int(start_date.split("/")[1])
    finish_month = int(finish_date.split("/")[1])
    start_year = int(start_date.split("/")[0])
    finish_year = int(finish_date.split("/")[0])
    if start_year == finish_year:
        if start_month == 1 or start_month == 2 or start_month == 3 or start_month == 4 or start_month == 5 or start_month == 6:
            startdate = int(start_month) * 31 + int(start_day)
        elif start_month == 7 or start_month == 8 or start_month == 9 or start_month == 10 or start_month == 11:
            startdate = int(start_month) * 30 + int(start_day)
        else:
            if start_year == 1403:
                startdate = int(start_month) * 30 + int(start_day)
            else:
                startdate = int(start_month) * 29 + int(start_day)
        if finish_month == 1 or finish_month == 2 or finish_month == 3 or finish_month == 4 or finish_month == 5 or finish_month == 6:
            finishdate = int(finish_month) * 31 + int(finish_day)
        elif finish_month == 7 or finish_month == 8 or finish_month == 9 or finish_month == 10 or finish_month == 11:
            finishdate = int(finish_month) * 30 + int(finish_day)
        else:
            if start_year == 1403:
                startdate = int(start_month) * 30 + int(start_day)
            else:
                startdate = int(start_month) * 29 + int(start_day)

        if int(start_month) == 11:
            if int(finish_month) == 12:
                total_day = int(finishdate) - int(startdate) - 1
                print("total_day ::::::::::::::::::")
                print(total_day)
                total_price = room_price * total_day
                print("total_price ::::::::::::::::::")
                print(total_price)
        else:
            total_day = int(finishdate) - int(startdate)
            print("total_day :::::::::::::::::::")
            print(total_day)
            total_price = room_price * total_day
            print("total_price ::::::::::::::::")
            print(total_price)
    else:
        if start_month == 1 or 2 or 3 or 4 or 5 or 6:
            startdate = 31 - int(start_day)
        elif start_month == 7 or 8 or 9 or 10 or 11:
            startdate = 30 - int(start_day)
        else:
            startdate = 29 - int(start_day)

        if finish_month == 1 or 2 or 3 or 4 or 5 or 6:
            finishdate = 31 - (31 - int(finish_day))
        elif finish_month == 7 or 8 or 9 or 10 or 11:
            finishdate = 30 - (30 - int(finish_day))
        else:
            finishdate = 29 - (29 - int(finish_day))

        total_day = int(finishdate) + int(startdate) - 1
        print("total_day :00000000000000000")
        print(total_day)
        total_price = room_price * total_day
        print("total_price :00000000000000000")
        print(total_price)

    return total_day, total_price


def reserve_error_day(request, start_date, finish_date, room_id):
    today_jalali = JalaliDate.today()
    this_year = today_jalali.year
    this_month = today_jalali.month
    today = today_jalali.day

    start_day = int(start_date.split("/")[2])
    finish_day = int(finish_date.split("/")[2])
    start_month = int(start_date.split("/")[1])
    finish_month = int(finish_date.split("/")[1])
    start_year = int(start_date.split("/")[0])
    finish_year = int(finish_date.split("/")[0])

    # Check if the end date is before the start date
    if finish_year < start_year or (finish_year == start_year and (
            finish_month < start_month or (finish_month == start_month and finish_day < start_day))):
        messages.error(request, 'تاریخ ورود نمی تواند بعد از تاریخ خروج باشد !')
        return True

    # Check if the dates are in the past
    if start_year < this_year or (start_year == this_year and (
            start_month < this_month or (start_month == this_month and start_day < today))):
        messages.error(request, 'تاریخ انتخابی رد شده است !')
        return True

    if finish_year < this_year or (finish_year == this_year and (
            finish_month < this_month or (finish_month == this_month and finish_day < today))):
        messages.error(request, 'در انتخاب تاریخ دقت کنید !')
        return True

    # Check if the start and end dates are the same
    if start_day == finish_day and start_month == finish_month and start_year == finish_year:
        messages.error(request, 'تاریخ ورود و خروج نمی تواند یکسان باشد !')
        return True

    # Check if the room is already reserved for the given dates
    existing_reserves = Reserve.objects.filter(room_id=room_id, start_date__lte=finish_date,
                                               finish_date__gte=start_date)
    if existing_reserves.exists():
        messages.error(request, 'اتاق در این تاریخ رزرو شده و امکان رزرو مجدد ندارد !')
        return True

    return False


def room_details(request, id):
    global room
    room = get_object_or_404(Room, id=id)
    option = room.option.all()
    filter_date_room = Reserve.objects.filter(room_id=id)
    reservations = [{'start_date': res.start_date, 'finish_date': res.finish_date} for res in filter_date_room]

    if request.method == 'POST':
        name = request.POST.get('name')
        request.session['namee'] = name
        family = request.POST.get('family')
        request.session['familyy'] = family

        start_date = request.POST.get('start_date')
        request.session['start_datee'] = start_date
        finish_date = request.POST.get('finish_date')
        request.session['finish_datee'] = finish_date
        foodCheckbox = request.POST.get('food')

        total_day, total_price = calculate_reserve_day(start_date, finish_date, room.price)

        if reserve_error_day(request, start_date, finish_date, id):
            return redirect('app:room_details', id)
        reserve = Reserve.objects.create(name=name, family=family, start_date=start_date, finish_date=finish_date,
                                         room_id=id, total_price=total_price)
        if foodCheckbox == 'True':
            return redirect('app:restaurant', reserve.id)
        else:
            return redirect('app:checkout', reserve.id)

    context = {
        'name': room.name,
        'number': room.number,
        'reservations': reservations,
        'floor': room.floor,
        'suggested': room.suggested,
        'price': room.price,
        'capacity': room.capacity,
        'image': room.image,
        'description': room.description,
        'option': room.option.all()
    }

    return render(request, 'room/room-details.html', context)


def services_1(request):
    return render(request, 'service/services-1.html')


def team(request):
    return render(request, 'team/team.html')


def terms_condition(request):
    return render(request, 'terms-condition/terms-condition.html')


def show_comment(request):
    showvip = Contact.objects.filter(show_in_comments_two=True)
    show = Contact.objects.filter(show_in_comments=True)
    context = {
        'show': show,
        'showvip': showvip
    }
    return render(request, 'show-comment/show-comment.html', context)


def calculate_total_price(food_reserve, num_food=None):
    global total_f_price, foood_num, fff
    total_f_price = 0
    foood_num = 0
    fff = None

    for res in food_reserve:
        food = Food.objects.get(id=res.food_id)
        ff = FoodReserve.objects.filter(reserve_id=res.reserve_id, food=food).first()
        fooood_num = FoodReserve.objects.filter(reserve_id=res.reserve_id, food=food).first()
        foood_num = int(fooood_num.num_food)
        if foood_num > 0:
            if ff:
                fff = ff.num_food
                total_f_price += food.price * int(fff)
            else:
                total_f_price += food.price
        else:
            print("false")
    return total_f_price, fff

def restaurant(request, id):
    global breakfast, lunch, dinner, foodres, total_food_price, total_food_price_with_num, fff
    breakfast = Food.objects.filter(foodType='0', status='1')
    lunch = Food.objects.filter(foodType='1', status='1')
    dinner = Food.objects.filter(foodType='2', status='1')
    num_food = request.POST.get('num_food')
    food_reserve = FoodReserve.objects.filter(reserve_id=id)
    foodres = []
    reserve_id = id

    for res in food_reserve:
        food = Food.objects.get(id=res.food_id)
        foodres.append((food.name, food.foodType, food.price, res.food_id, res.num_food))

    total_food_price, fff = calculate_total_price(food_reserve, num_food)
    total_food_price_with_num = total_food_price

    if request.method == 'POST':
        delete = request.POST.get('delete')
        foodId = request.POST.get('food')
        finish = request.POST.get('submit')

        if finish == 'True':
            return redirect('app:checkout', id)
        elif delete:
            food_delete = FoodReserve.objects.filter(food_id=delete, reserve_id=id).first()
            if food_delete:
                food_delete.delete()
            return redirect('app:restaurant', id)
        else:
            if foodId and num_food:
                FoodReserve.objects.create(food_id=foodId, num_food=num_food, reserve_id=id)
                reserve = Reserve.objects.get(id=id)
                food = Food.objects.get(id=foodId)
                reserve.total_price += food.price
                reserve.save()
            return redirect('app:restaurant', id=reserve_id)

    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'food_reserve': foodres,
        'capacity': room.capacity,
        'total_day': total_day,
        'total_food_price': total_food_price,
        'total_food_price_with_num': total_food_price_with_num,
        'fff': fff,
        'foood_num': foood_num
    }

    return render(request, 'restaurant/restaurant.html', context)


def checkout(request, id):
    if request.method == 'POST':
        city = request.POST.get('city')
        request.session['city'] = city
        address = request.POST.get('address')
        request.session['address'] = address

        state = request.POST.get('state')
        request.session['state'] = state

        global phone
        phone = request.POST.get('phone')
        global random_code
        random_code = request.POST.get('random_code')
        email = request.POST.get('email')
        try:
            reserve = Reserve.objects.filter(id=id).update(state=state, city=city, address=address, email=email)
        except:
            pass
        form = LoginPhoneForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            phone = f"{data['phone']}"
            request.session['phone'] = phone

            random_code = random.randint(10000, 99999)
            sms = KavenegarAPI(
                "******************************************************************")
            params = {
                'sender': '****************',  # Array of String
                'receptor': phone,  # Array of String
                'message': f' \n کد تایید شما برای رزرو در هتل :  {random_code}'
                           f' اگر شما درخواست رزرو اتاق ندادید نیاز به انجام کاری نیست.',

            }
            print(random_code)
            response = sms.sms_send(params)
            return redirect('app:verify_phone', reserve_id=id)
    else:
        total_f_price = 0
        form = LoginPhoneForm()
        context = {
            'form': form,
            'total_price': total_price,
            'capacity': room.capacity,
            'name': room.name,
            'number': room.number,
            'floor': room.floor,
            'suggested': room.suggested,
            'price': room.price,
            'capacity': room.capacity,
            'image': room.image,
            'description': room.description,
        }
        if total_f_price is not None:
            context['total_f_price'] = total_f_price
    return render(request, 'checkout/checkout.html', context)


def verify_phone(request, reserve_id):
    global aaa, total_food_price_with_num
    if 'total_food_price_with_num' not in globals():
        total_food_price_with_num = 0
    if total_food_price_with_num == None or total_food_price_with_num == 0:
        aaa = total_price
    else:
        aaa = total_food_price_with_num + total_price
    if request.method == 'POST':
        form = CodePhoneForm(request.POST)
        if form.is_valid():
            if str(random_code) == form.cleaned_data['verify_code']:
                if str(random_code):
                    try:
                        Reserve.objects.filter(id=reserve_id).update(phone=phone, verify_code=random_code)
                        return redirect('app:bill')
                    except Reserve.DoesNotExist:
                        messages.error(request, 'رزرو یافت نشد')
            else:
                messages.error(request, 'کد وارد شده اشتباه است')
    else:
        form = CodePhoneForm()

    context = {
        'form': form,
        'total_food_price_with_num': total_food_price_with_num,
        'total_price': total_price,
        'aaa': aaa,
    }
    return render(request, 'checkout/verify-phone.html', context)


def bill(request):
    namee = request.session.get('namee')
    familyy = request.session.get('familyy')
    phone = request.session.get('phone')
    address = request.session.get('address')
    state = request.session.get('state')
    city = request.session.get('city')
    finish_datee = request.session.get('finish_datee')
    start_datee = request.session.get('start_datee')
    global breakfast, lunch, dinner, foodres, foood_num, fff
    if 'breakfast' not in globals():
        breakfast = None

    if 'lunch' not in globals():
        lunch = None

    if 'dinner' not in globals():
        dinner = None

    if 'foodres' not in globals():
        foodres = None

    if 'foood_num' not in globals():
        foood_num = None

    if 'fff' not in globals():
        fff = None
    context = {
        'name': room.name,
        'number': room.number,
        'price': room.price,
        'namee': namee,
        'familyy': familyy,
        'phone': phone,
        'address': address,
        'city': city,
        'state': state,
        'aaa': aaa,
        'startdate': start_datee,
        'finishdate': finish_datee,
        'total_price': total_price,
        'total_day': total_day,
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'food_reserve': foodres,
        'fff': fff,
        'foood_num': foood_num

    }

    return render(request, 'bill/bill.html', context)
