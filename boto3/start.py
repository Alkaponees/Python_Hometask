
import boto3
ec2 = boto3.resource('ec2')
# ubuntu="ami-012ae45a4a2d92750"
# amazon="ami-0917076ab9780844d"
def create_instance(image,instanceType,keyName):
    instances = ec2.create_instances(
        Monitoring={
            'Enabled':True
        },
        ImageId=image,
        MinCount=1,
        MaxCount=1,
        InstanceType=instanceType,
        KeyName=keyName,
        SecurityGroupIds=[
        'sg-05eefaef33dc0600c'
    ],
    )

print("Welcome to AWS")

run = False
while run != True:
        choice=int(input("Make your choice (1.Create instance 0.Exit)"))
        if choice == 1:
            image=(input("Enter image ami(\n1.Ubuntu-ami-012ae45a4a2d92750 \n2.Amazon-ami-0917076ab9780844d)\n"))
            instanceType=(input("Enter instance type (\nt3.micro\nt2.micro) "))
            keyName=(input("Enter keyName (Stockholm_RSA) "))
        elif choice == 0:
            run = True  
        else:
            print("You enter invalid value!!!!")

create_instance(image,instanceType,keyName)

