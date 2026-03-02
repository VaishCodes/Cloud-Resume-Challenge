###### **AWS Cloud Resume Challenge – Vaishnavi Raghavan**

*This repository contains my implementation of the Cloud Resume Challenge (AWS edition) – a hands‑on project where I turned my resume into a cloud‑hosted, serverless application.*



**Live site**

Resume: https://d2dvuqgzyddbf.cloudfront.net



**Architecture overview**

This project uses a simple serverless architecture on AWS:



**Frontend**



* HTML/CSS single‑page resume.
* Hosted on Amazon S3 using static website hosting.
* Served globally via Amazon CloudFront for edge caching and improved performance.



**Backend (visitor counter)**



* AWS Lambda function to read and update a visitor count.
* Amazon DynamoDB table to persist the count.
* Exposed via an HTTP endpoint and consumed from the frontend using JavaScript.



**Security \& access**



* AWS IAM used to create a least‑privilege user for GitHub Actions, with scoped S3 and CloudFront permissions.



**Automation / CI‑CD**



* Source control with Git + GitHub.
* GitHub Actions workflow that:
* Syncs frontend files to S3.
* Automatically runs a CloudFront cache invalidation (/\*) after each push to main.



**Technologies used**

AWS: S3, CloudFront, Lambda, DynamoDB, IAM

CI/CD: Git, GitHub Actions

Frontend: HTML, CSS, JavaScript



**Deployment (high‑level)**

* Commit and push changes to the main branch.
* GitHub Actions workflow:
* Checks out the repo.
* Syncs updated files to the S3 bucket.
* Calls aws cloudfront create-invalidation --paths "/\*" for the distribution.
* CloudFront retrieves fresh content from S3 and serves the new version globally.



***About the Cloud Resume Challenge***

The Cloud Resume Challenge, created by Forrest Brazeal, is a multi‑step project designed to help people move from cloud certification towards real, demonstrable experience by building a resume website using cloud‑native services, serverless components, automation, and Infrastructure as Code.

