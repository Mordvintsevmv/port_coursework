from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import json

file = open("port_data.json", "r", encoding="utf8")
text = file.read()
file.close()
data = json.loads(text)
seaport_data = []
seaport_data.extend(data)

port_name = ""
warning = "Вы что-то не ввели! Проверьте ещё раз!"
ID_warning = "Вы ввели уже существующую транспортировку!"
success = "Вы удачно добавили транспортирвку!"
start = "Добавьте новую транспортировку!"
user_warning = "Вы добавляете уже существующего пользователя!"
user_success = "Вы удачно добавили пользователя!"
user_start = "Добавьте нового пользователя!"


file = open("user_data.json", "r", encoding="utf8")
text = file.read()
file.close()
user_json = json.loads(text)
user_data = []
user_data.extend(user_json)

def index(request):
    args = {}
    args["username"] = auth.get_user(request).username
    u = auth.get_user(request)
    return render(request, 'index.html', {
        "username": auth.get_user(request).username,
    })


def all_transport(request):
    args = {}
    args["username"] = auth.get_user(request).username
    u = auth.get_user(request)
    check = u.is_authenticated

    return render(request, 'all_transport.html', {
        "seaport_data": seaport_data,
        "username": auth.get_user(request).username,
        "check": check
    })


def port_search(request):
    args = {}
    args["username"] = auth.get_user(request).username
    u = auth.get_user(request)
    check = u.is_authenticated
    if request.method == "POST":
        port_name = request.POST.get("port")
        return render(request, 'port_search.html', {
            "port_name": port_name,
            "seaport_data": seaport_data,
            "username": auth.get_user(request).username,
            "check": check
        })
    else:
        return render(request, 'port_search.html', {
            "seaport_data": seaport_data,
            "username": auth.get_user(request).username,
            "check": check
        })


def in_port(request):
    args = {}
    args["username"] = auth.get_user(request).username
    u = auth.get_user(request)
    check = u.is_authenticated
    if request.method == "POST":
        port_name = request.POST.get("port")
        return render(request, 'in_port.html', {
            "port_name": port_name,
            "seaport_data": seaport_data,
            "username": auth.get_user(request).username,
            "check": check
        })
    else:
        return render(request, 'in_port.html', {
            "seaport_data": seaport_data,
            "username": auth.get_user(request).username,
            "check": check
        })


def out_port(request):
    args = {}
    args["username"] = auth.get_user(request).username
    u = auth.get_user(request)
    check = u.is_authenticated
    if request.method == "POST":
        port_name = request.POST.get("port")
        return render(request, 'out_port.html', {
            "port_name": port_name,
            "seaport_data": seaport_data,
            "username": auth.get_user(request).username,
            "check": check
        })
    else:
        return render(request, 'out_port.html', {
            "seaport_data": seaport_data,
            "username": auth.get_user(request).username,
            "check": check
        })


def transport_search(request):
    u = auth.get_user(request)
    check = u.is_authenticated
    if request.method == "POST":
        trasnport = request.POST.get("transport")
        return render(request, 'transport_search.html', {
            "transport": trasnport,
            "seaport_data": seaport_data,
            "username": auth.get_user(request).username,
            "check": check
        })
    else:
        return render(request, 'transport_search.html', {
            "seaport_data": seaport_data,
            "username": auth.get_user(request).username,
            "check": check
        })


def edit(request):
    args = {}
    args["username"] = auth.get_user(request).username
    u = auth.get_user(request).username
    check = False
    for i in range(0,len(user_data)):
        if (u == user_data[i]["username"]):
            if (user_data[i]["permission"] == "Stuff" or user_data[i]["permission"] == "Admin"):
                check = True

    if request.method == "POST":
        port_name = request.POST.get("port_name")
        ID = request.POST.get("ID")
        sudno = request.POST.get("sudno")
        model = request.POST.get("model")
        type = request.POST.get("type")
        charac = request.POST.get("charac")
        port_out = request.POST.get("port_out")
        time_out = request.POST.get("time_out")
        port_in = request.POST.get("port_in")
        time_in = request.POST.get("time_in")

        for i in range(0, len(seaport_data)):
            for j in range(0, len(seaport_data[i]["transport"])):
                if (ID == seaport_data[i]["transport"][j]["id"]):
                    return render(request, 'edit.html', {
                        "ID_warning": ID_warning,
                        "username": auth.get_user(request).username,
                        "check": check
                    })

        if (port_name == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (ID == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (sudno == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (model == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (type == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (charac == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (port_out == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (time_out == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (port_in == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (port_out == ""):
            return render(request, 'edit.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })

        else:

            zagr = [{
                "name_port": port_name,
                "transport":
                    [
                        {
                            "id": ID,
                            "sudno": [
                                {
                                    "name_sudno": sudno,
                                    "model": model,
                                    "type": type,
                                    "char": charac
                                }
                            ],
                            "out_punkt": [
                                {
                                    "name_port": port_out,
                                    "out_time": time_out
                                }
                            ],
                            "in_punkt": [
                                {
                                    "name_port": port_in,
                                    "in_time": time_in
                                }
                            ]

                        }
                    ]
            }]

            zagr_same_port = [{
                "id": ID,
                "sudno": [
                    {
                        "name_sudno": sudno,
                        "model": model,
                        "type": type,
                        "char": charac
                    }
                ],
                "out_punkt": [
                    {
                        "name_port": port_out,
                        "out_time": time_out
                    }
                ],
                "in_punkt": [
                    {
                        "name_port": port_in,
                        "in_time": time_in
                    }
                ]
            }]

            flag = 0
            for i in range(0, len(seaport_data)):
                if (port_name == seaport_data[i]["name_port"]):
                    seaport_data[i]["transport"].extend(zagr_same_port)
                    file = open("port_data.json", "w", encoding="utf8")
                    data = json.dumps(seaport_data)
                    file.write(data)
                    file.close()
                    flag = 1
                    break

            if (flag == 0):
                seaport_data.extend(zagr)
                file = open("port_data.json", "w", encoding="utf8")
                data = json.dumps(seaport_data)
                file.write(data)
                file.close()

            return render(request, 'edit.html', {
                "success": success,
                "username": auth.get_user(request).username,
                "check": check
            })
    else:
        return render(request, 'edit.html', {
            "start": start,
            "username": auth.get_user(request).username,
            "check": check
        })


def login(request):
    login_error = "Такого пользователя не существует! Проверьте логин/пароль."
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        f = True

        for i in range(0, len(user_data)):
            if ((username == user_data[i]["username"]) and (password == user_data[i]["password"])):
                f = False
                user = auth.authenticate(username=username, password=password)
                if (user is None):
                    user = User.objects.create_user(username=username, password=password)
                    auth.login(request, user)
                    return render(request, "index.html", {"username": auth.get_user(request).username, })
                else:
                    auth.login(request, user)
                    return render(request, "index.html", {"username": auth.get_user(request).username, })

        if (f):
            return render(request, "login.html",
                          {"username": auth.get_user(request).username, "login_error": login_error})
    else:
        return render(request, 'login.html', {"username": auth.get_user(request).username, })


def logout(request):
    args = {}
    args["username"] = auth.get_user(request).username
    auth.logout(request)
    return render(request, "index.html", {"username": auth.get_user(request).username, })

def add_user(request):
    u = auth.get_user(request).username
    check = False
    for i in range(0,len(user_data)):
        if (u == user_data[i]["username"]):
            if (user_data[i]["permission"] == "Admin"):
                check = True

    if request.method == "POST":
        nusername = request.POST.get("username")
        npassword = request.POST.get("password")
        nphone = request.POST.get("phone")
        nemail = request.POST.get("email")
        nname = request.POST.get("name")
        nsurname = request.POST.get("surname")
        ngender = request.POST.get("gender")
        npermission = request.POST.get("permission")

        for i in range(0, len(user_data)):
                if (nusername == user_data[i]["username"]):
                    return render(request, 'add_user.html', {
                        "user_warning": user_warning,
                        "username": auth.get_user(request).username,
                        "check": check
                    })

        if (nusername == ""):
            return render(request, 'add_user.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (npassword == ""):
            return render(request, 'add_user.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (nphone == ""):
            return render(request, 'add_user.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (nemail == ""):
            return render(request, 'add_user.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (nname == ""):
            return render(request, 'add_user.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (nsurname == ""):
            return render(request, 'add_user.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (ngender == ""):
            return render(request, 'add_user.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })
        elif (npermission == ""):
            return render(request, 'add_user.html', {
                "warning": warning,
                "username": auth.get_user(request).username,
                "check": check
            })


        else:

            zagr = [{
                "username": nusername,
                "password":npassword,
                "phone": nphone,
                "email": nemail,
                "name": nname,
                "surname": nsurname,
                "gender": ngender,
                "permission": npermission
            }]



            user_data.extend(zagr)
            file = open("user_data.json", "w", encoding="utf8")
            data = json.dumps(user_data)
            file.write(data)
            file.close()

            return render(request, 'add_user.html', {
                "user_success": user_success,
                "username": auth.get_user(request).username,
                "check": check
            })
    else:
        return render(request, 'add_user.html', {
            "user_start": user_start,
            "username": auth.get_user(request).username,
            "check": check
        })

