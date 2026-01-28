# Text Narrator Using Amazon Polly

##  Project Overview
This project demonstrates a serverless text-to-speech application using Amazon Polly, AWS Lambda, and Amazon S3. The system converts input text into natural-sounding speech and stores the generated audio file in an S3 bucket.

---

##  Technologies Used
- AWS Lambda (Python 3.10)
- Amazon Polly
- Amazon S3
- AWS IAM

---

##  Architecture
1. AWS Lambda receives the input text
2. Amazon Polly converts text to speech
3. Generated audio file is stored in Amazon S3

---

##  Workflow
- Lambda function triggers Amazon Polly
- Polly generates MP3 audio
- Lambda uploads audio to S3
- User downloads or plays the audio file

---

##  Project Structure

text-narrator-amazon-polly/
│
├── lambda_function.py
└── README.md

##  How to Run
1. Create an S3 bucket
2. Create an IAM role with Polly and S3 permissions
3. Create a Lambda function using Python
4. Deploy the code and test the function
5. Check the generated MP3 file in S3

---

##  Real-Time Use Cases
- Accessibility tools for visually impaired users
- Voice assistants
- E-learning platforms
- Customer support IVR systems
- Audio content generation

---

##  Future Enhancements
- API Gateway integration
- Dynamic text input
- Multi-language support
- Web UI integration

---




