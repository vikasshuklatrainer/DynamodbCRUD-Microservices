# Dynamodb CRUD-Micro services(Lambda)

# What we are going to build 

![What we are building](./images/What-we-are-building.png)



## Lets Create a AWS DynamoDB Table

```html
STEP 1 — Create DynamoDB Table

Open DynamoDB → Tables → Create table

Table name: Students

Partition key:

Name: studentId

Type: String

Leave defaults → Create table


```

![Create dynamo db table](./images/Create-dynamo-db-table.png)

## STEP 2 — Create IAM Role for Lambda

![Create Iam 1](./images/create-iam-1.png)

![Create Iam 2](./images/create-iam-2.png)

![Create Iam 3](./images/create-iam-3.png)

Create the role. This role will be assigned during creation of lambda functions.

## Create Lambda Functions as micro services

Lets create 4 lamda functions, we will use above created IAM role.
![4 Lambda Functions](./images/4-lambda-functions.png)

![Lambda Creations](./images/lambda-creations.png)

![lambda](./images/lambda.png)

you can use the code from the repo.


## To Enable the communication
from this static page to our lambda functions, we need to change the configuration in every lambda function.

![Edit Configuration](./images/edit-configuration.png)

![Enabling Config](./images/enabling-config.png)


After changing , it should look like this

![After cors enabling](./images/After-cors-enabling.png)

Finally our application looks like 

![What we are building](./images/What-we-are-building.png)


# Lets Expose these lambda by AWS API Gateway
