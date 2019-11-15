# Comparison of FaaS Technologies
Comparision of Cloud Platforms based on Serverless Computing (FaaS)
This project primarily focuses on the three main FaaS competitors i.e. Amazon Web Services, Microsoft Azure and Google Cloud Platform. AWS provides FaaS offerings as AWS Lambda, Azure provides Azure Functions and GCP has Google Cloud Functions. The aim is to provide a comparative analysis of the three available solutions based on the parameters like throughput, latency, and cold start statistics.

- Python
- Apache JMeter
- Postman

## Azure Function
For Implementing the Azure functions in python we had to adopt the following approach:
- Installed the Azure FunctionsCore Tools to build and test locally
- Created and activated a virtual environment
- Created a local functions project with worker runtime as Python
- Developed an HTTP trigger based Function which converts JSON to XML and then tested the code locally
- Then Deployed the code using Azure CLI
- Created a resource group and an Azure Storage account

` az group create --name deepakResourceGroup8 --location westeurope
az storage account create --name memx --location westeurope --resource-group deepakResourceGroup8 --sku Standard_LRS`

- This was followed by creating a Linus function App

`az functionapp create --resource-group deepakResourceGroup8 --os-type Linux \ --consumption-plan-location westeurope  --runtime python \   --name jxconverter --storage-account memx`
- Finally, Deployed the function app project to Azure

`func azure functionapp publish jxconverter`

## AWS Lambda
For writing Lambda functions following steps were followed:
- After logging in to AWS account, navigate to Lambda console
- Select creating a function from scratch option, i.e. Author from scratch
- Ensure the correct availability region is selected from the top-right corner
- Enter information such as Function name, Runtime (Python 3.7), and select the existing role
- API gateway is added as a trigger and a resource with POST action is created
- Configure Method Request, Integration Request, Method Response, and Integration Response
- Once ready the API can be tested and deployed which generates an API endpoint

## Google Cloud Function
For writing Google Cloud functions following steps were followed:
- After logging in to GCP account, navigate to Cloud functions
- Select “Create Function” option and enter the information such as function name, trigger as HTTP, Runtime as Python 3.7 and region
- Once the function is written, it generates an HTTP URL which acts as a trigger for invoking the function

## Results
### Test 1
- Concurrent Requests = 5
- Repetition of Loop = 2
- Total number of Requests = 10


| Label                  | #Samples | Average | Min  | Max   | Std. Dev. | 95% Line | 99% Line | Throughput | Received KB/sec | Sent KB/sec | Avg. Bytes |
|------------------------|----------|---------|------|-------|-----------|----------|----------|------------|-----------------|-------------|------------|
| AWS Lambda Request     | 10       | 3400    | 2862 | 4041  | 317.52    | 3654     | 4041     | 0.4555     | 327.05          | 347.56      | 735239     |
| GCF Request            | 10       | 3815    | 3562 | 4388  | 243.8     | 4026     | 4388     | 0.44462    | 319.22          | 339.26      | 735191.8   |
| Azure Function Request | 10       | 7547    | 2371 | 14179 | 4207.31   | 10934    | 14179    | 0.31444    | 225.79          | 239.93      | 735298.4   |

### Test 2
- Concurrent Requests = 5
- Repetition of Loop = 2
- Total number of Requests = 100

| Label                  | #Samples | Average | Min  | Max   | Std. Dev. | 95% Line | 99% Line | Throughput | Received KB/sec | Sent KB/sec | Avg. Bytes |
|------------------------|----------|---------|------|-------|-----------|----------|----------|------------|-----------------|-------------|------------|
| AWS Lambda Request     | 100      | 3157    | 2783 | 6061  | 350.88    | 3564     | 3810     | 0.49217    | 353.38          | 375.54      | 735239     |
| GCF Request            | 100      | 3652    | 3372 | 5555  | 281.28    | 4210     | 4438     | 0.49248    | 353.58          | 375.77      | 735191.7   |
| Azure Function Request | 100      | 3250    | 2288 | 14676 | 2756.93   | 13246    | 14587    | 0.49378    | 354.57          | 376.78      | 735318.4   |


### Test 3
- Concurrent Requests = 1
- Repetition of Loop = 100
- Total number of Requests = 100

| Label                  | #Samples | Average | Min  | Max   | Std. Dev. | 95% Line | 99% Line | Throughput | Received KB/sec | Sent KB/sec | Avg. Bytes |
|------------------------|----------|---------|------|-------|-----------|----------|----------|------------|-----------------|-------------|------------|
| AWS Lambda Request     | 100      | 3053    | 2825 | 4973  | 306.14    | 3265     | 4637     | 0.10471    | 75.18           | 79.89       | 735239     |
| GCF Request            | 100      | 3634    | 3416 | 4229  | 156.31    | 3887     | 4221     | 0.10472    | 75.18           | 79.9        | 735193.2   |
| Azure Function Request | 100      | 2905    | 2290 | 13095 | 1113.91   | 3886     | 4552     | 0.10481    | 75.26           | 79.97       | 735314.1   |

