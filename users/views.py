import json
import bcrypt
import jwt

from django.http              import JsonResponse
from django.views             import View
from core.utils               import *

from django.core.exceptions   import ValidationError 
from wesop.settings           import SECRET_KEY,ALGORITHM
from core.validator import *

from users.models import *


class SignupView(View): 
    def post(self,request):
        
        try:
            
            data       = json.loads(request.body)   
            email      = data['email'] 
            first_name = data['first_name'] 
            last_name  = data['last_name']
            password   = data['password']
            
            
            if User.objects.filter(email = email).exists():
             return JsonResponse({"message":"DUPLICATE_EMAIL"}, status = 400)
            
            validate_email(email)
            validate_name(first_name)
            validate_name(last_name)
            validate_password(password)
            
            User.objects.create(
                    skin_type    = Skintype.objects.get(skin_type=data['skin_type']),
                    first_name   = first_name,
                    last_name    = last_name,
                    email        = email,
                    password     = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            )
            
            
            return JsonResponse({"message":"SUCCESS"}, status = 200)
       
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)
        except ValidationError as e :
            return JsonResponse({'message' : e.message }, status = 400)
        
            
    def get(self, request):
        return JsonResponse({'results':list(User.objects.values())},status = 200)
    
class SigninView(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)
            password = data['password']
            email    = data['email']
            
            if not bcrypt.checkpw(password.encode('utf-8'), User.objects.get(email = data['email']).password.encode('utf-8')):
                return JsonResponse({"message": "INVALID_USER"}, status = 401)
            
            token  = jwt.encode({'email':email}, SECRET_KEY, ALGORITHM)
            
            
            return JsonResponse({"access_token":token},status=201)
        
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=401)