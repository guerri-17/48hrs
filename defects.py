# 48 hours - Generative AI
# 04-12-23 Project Defects Resolutor (DR) using Google LLM enterprise Vertex.

import requests

newLine = "\n"

print("\nDoes this JIRA defect have a reference to Azure in the problem statement?\n")

data = {
  "instances": [
    "Provide the number of this defect: Defect 160704 is using Azure and Multi-Factor authentication for our organization with Dimensions.\n  Application loops in the sign in process where once someone approves or authenticates themselves within Microsoft authenticator tool and goes back to the Dimensions application, they are prompted again to authenticate.\nThis seems to be isolated to employees who are using MFA and the Dimensions application on the same device and are moving back and forth between applications.",
    "Does this defect have a reference to Azure?: Defect 160704 is using Azure and Multi-Factor authentication for our organization with Dimensions.\n  Application loops in the sign in process where once someone approves or authenticates themselves within Microsoft authenticator tool and goes back to the Dimensions application, they are prompted again to authenticate.\nThis seems to be isolated to employees who are using MFA and the Dimensions application on the same device and are moving back and forth between applications.",
    "Provide the number of this defect: Defect 156856 is logging on to the UKG app via iPhone, the Microsoft Authenticator app is used to complete MFA authentication for SSO. Once complete, the MS Authenticator app stays open on the screen and does not switch back to the UKG app. \n At the very top of the screen, there is a very thin bar with a back arrow and METEOR, which is frequently not observed by users. If you click back it will take you into the UKG app and you can access data OK.",  
    "Does this defect have a reference to Azure?: Defect 156856 is logging on to the UKG app via iPhone, the Microsoft Authenticator app is used to complete MFA authentication for SSO. Once complete, the MS Authenticator app stays open on the screen and does not switch back to the UKG app. \n At the very top of the screen, there is a very thin bar with a back arrow and METEOR, which is frequently not observed by users. If you click back it will take you into the UKG app and you can access data OK.",  
    "Provide the number of this defect: Defect 149577 is using Azure as an IDP and authenticating into mobile app via SSO with MFA. When navigating to MS Authenticator app to approve MFA, intermittently, the user is not logged into WFD. They are displayed the IDP logon page again. Only happens for iOS devices.", 
    "Does this defect have a reference to Azure?: Defect 149577 is using Azure as an IDP and authenticating into mobile app via SSO with MFA. When navigating to MS Authenticator app to approve MFA, intermittently, the user is not logged into WFD. They are displayed the IDP logon page again. Only happens for iOS devices.",  
  ],
  'temperature': 0.2
}
response = requests.post('http://130.211.213.132/predict', json=data)
print(response.json())

print("\nList the steps to reproduce this JIRA defect.\n")

data = {
    "instances":[
    "Provide the number of this defect: Defect 160764 - The problem was reported by a customer, but cannot be reproduced in any other tenant. The steps below are how the customer makes the issue happen on their own tenant - \nIf this issue is not a feature request or documentation/Help defect, then a database schema backup will be provided for Engineering to use to stage a Tenant to be used with the Steps to Reproduce below - \n1. Login to Dimensions on the Mobile Device \n2. Authenticate through Microsoft\n3.Go back to Dimensions App\n4: You are prompted to Authenticate again",
    "Locate the sentences that are numbered: Defect 160764 - The problem was reported by a customer, but cannot be reproduced in any other tenant. The steps below are how the customer makes the issue happen on their own tenant - \nIf this issue is not a feature request or documentation/Help defect, then a database schema backup will be provided for Engineering to use to stage a Tenant to be used with the Steps to Reproduce below - \n1. Login to Dimensions on the Mobile Device \n2. Authenticate through Microsoft\n3.Go back to Dimensions App\n4: You are prompted to Authenticate again"
    ]
}
response = requests.post('http://130.211.213.132/predict', json=data)
print(response.json())
print(newLine)

data = {
    "instances": [
    "Provide the number of this defect: Defect 156856 - The problem was reported by a customer, but cannot be reproduced in any other tenant. The steps below are how the customer makes the issue happen on their own tenant - \nIf this issue is not a feature request or documentation/Help defect, then a database schema backup will be provided for Engineering to use to stage a Tenant to be used with the Steps to Reproduce below - \n1. Open the UKG app\n2. Choose an account to log in\n3. User will be taken to Microsoft Authenticator to complete the authentication\n4. Once completed, Authenticator stays open on screen and doesn't switch back to the UKG app.",
    "Locate the sentences that are numbered: Defect 156856 - The problem was reported by a customer, but cannot be reproduced in any other tenant. The steps below are how the customer makes the issue happen on their own tenant - \nIf this issue is not a feature request or documentation/Help defect, then a database schema backup will be provided for Engineering to use to stage a Tenant to be used with the Steps to Reproduce below - \n1. Open the UKG app\n2. Choose an account to log in\n3. User will be taken to Microsoft Authenticator to complete the authentication\n4. Once completed, Authenticator stays open on screen and doesn't switch back to the UKG app.",
  ]
}
response = requests.post('http://130.211.213.132/predict', json=data)
print(response.json())
print(newLine)

data = {
  "instances": [
    "Provide the number of this defect: Defect 149577 - The problem was reported by a customer, but cannot be reproduced in any other tenant. The steps below are how the customer makes the issue happen on their own tenant - \nIf this issue is not a feature request or documentation/Help defect, then a database schema backup will be provided for Engineering to use to stage a Tenant to be used with the Steps to Reproduce below:\n1. Open Mobile App\n2. Enter credentials on IDP logon page\n3. Be prompted for MFA, navigate to Google Authenticator app to satisfy MFA\n4. Navigate back to Mobile App\n5. User is intermittently logged into WFD, sometimes being sent back to the IDP logon page",
    "Locate the sentences that are numbered: Defect 149577 - The problem was reported by a customer, but cannot be reproduced in any other tenant. The steps below are how the customer makes the issue happen on their own tenant - \nIf this issue is not a feature request or documentation/Help defect, then a database schema backup will be provided for Engineering to use to stage a Tenant to be used with the Steps to Reproduce below:\n1. Open Mobile App\n2. Enter credentials on IDP logon page\n3. Be prompted for MFA, navigate to Google Authenticator app to satisfy MFA\n4. Navigate back to Mobile App\n5. User is intermittently logged into WFD, sometimes being sent back to the IDP logon page"
  ]
}
response = requests.post('http://130.211.213.132/predict', json=data)
print(response.json())
