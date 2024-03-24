from django.shortcuts import render
from rest_framework import viewsets


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .diabetes import predict_diabetes
from .heart_disease import predict_heart_disease
from .parkinsons import predict_parkinsons
import json
# Create your views here.





@csrf_exempt
def diabetes_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body.decode('utf-8'))

            # Extract the array of arrays from the request data
            input_arrays = json.loads(str(data["input_arrays"]))
            print(input_arrays)
            

            # # Process the arrays using the function from compute.py
            result = predict_diabetes(input_arrays)

            # # # Return the result as JSON response
            response_data = {'result': result}
            # # results = [str(sub_array) + 'abc' for sub_array in input_arrays]
            # # return results
            return JsonResponse(response_data)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
@csrf_exempt
def heart_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body.decode('utf-8'))

            # Extract the array of arrays from the request data
            input_arrays = json.loads(str(data["input_arrays"]))
            print(input_arrays)
            

            # # Process the arrays using the function from compute.py
            result = predict_heart_disease(input_arrays)

            # # # Return the result as JSON response
            response_data = {'result': result}
            # # results = [str(sub_array) + 'abc' for sub_array in input_arrays]
            # # return results
            return JsonResponse(response_data)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
@csrf_exempt
def parkinson_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body.decode('utf-8'))

            # Extract the array of arrays from the request data
            input_arrays = json.loads(str(data["input_arrays"]))
            print(input_arrays)
            

            # # Process the arrays using the function from compute.py
            result = predict_parkinsons(input_arrays)

            # # # Return the result as JSON response
            response_data = {'result': result}
            # # results = [str(sub_array) + 'abc' for sub_array in input_arrays]
            # # return results
            return JsonResponse(response_data)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

