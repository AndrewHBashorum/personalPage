from django.shortcuts import render

# Create your views here.
import boto3
from botocore.exceptions import ClientError
from django.http import HttpResponse
import os

from personal_page.settings import AWS_ACCESS_KEY_ID

def download_pdf(request):

    print(os.environ.get('AWS_ACCESS_KEY_ID'), '***', AWS_ACCESS_KEY_ID)
    s3 = boto3.client('s3',
                      aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))


    # Replace the values below with your own S3 bucket and file details 
    bucket = 'andrewbashorumsitebucket'
    key = 'Curriculum_Vitae_Andrew_Bashorum.pdf'

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
    except ClientError as e:
        return HttpResponse('The requested file does not exist.', status=404)

    # Set the appropriate headers for the download
    filename = key.split('/')[-1]
    response_headers = {
        'Content-Type': 'application/pdf',
        'Content-Disposition': f'attachment; filename="{filename}"',
        'Expires': '0',
        'Cache-Control': 'must-revalidate',
        'Pragma': 'public',
    }

    # Serve the file as a download
    return HttpResponse(response['Body'].read(), headers=response_headers)

def home(request):
    return render(request, 'pages/home.html')

def lanu(request):
    return render(request, 'pages/lanu.html')

def blog(request):
    return render(request, 'pages/blog.html')

def youtube(request):
    return render(request, 'pages/youtube.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def models(request):
    return render(request, 'pages/models.html')

def research(request):
    return render(request, 'pages/research.html')
