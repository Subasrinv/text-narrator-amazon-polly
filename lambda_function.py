import boto3
import uuid

def lambda_handler(event, context):
    polly = boto3.client('polly')
    s3 = boto3.client('s3')

    text = "Hello! This is Amazon Polly text to speech demo."

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    audio = response['AudioStream'].read()

    bucket_name = 'abcdef'
    file_name = f"polly_audio_{uuid.uuid4()}.mp3"

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=audio,
        ContentType='audio/mpeg'
    )

    return {
        'statusCode': 200,
        'body': 'Audio file generated successfully'
    }
