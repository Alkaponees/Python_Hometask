
import boto3

class Ec2_service:
    
    def __init__(self):
        self.ec2 = boto3.resource('ec2') 
        self.client= boto3.client('ec2')
    def show_security_groups(self):
        self.security_group=self.ec2.security_groups.all()
        print('Security Groups:')
        for group in self.security_group:
            print(f'  - Security Group {group.id} , Name: {group.group_name}')
    def add_security_groups(self,groupName):

        self.security_group=self.ec2.create_security_group(
            Description='Allow inbounded trafic',
            GroupName=groupName
        )
        self.security_group.authorize_ingress(
            CidrIp='0.0.0.0/0',
            FromPort=22,
            ToPort=22,
            IpProtocol='tcp')
        self.security_group.authorize_ingress(
            CidrIp='0.0.0.0/0',
            FromPort=80,
            ToPort=80,
            IpProtocol='tcp')
        self.security_group.authorize_ingress(
            CidrIp='0.0.0.0/0',
            FromPort=8080,
            ToPort=8080,
            IpProtocol='tcp')
    def delete_security_group(self,groupName):
        self.client.delete_security_group( 
            GroupName=groupName,
        )
        print(f'Security group {self.security_group.id} was deleted')
    def show_all_instance(self):
        for instance in self.ec2.instances.all():
         print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
             instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
            )
        )
    def create_instance_with_created_security_group(self,image,instanceType,keyName):
        self.instances =self.ec2.create_instances(
        Monitoring={
            'Enabled':True
        },
        ImageId=image,
        MinCount=1,
        MaxCount=1,
        InstanceType=instanceType,
        KeyName=keyName,
        SecurityGroupIds=[
        self.security_group.id],
        )
    def create_instance_with_attached_security_group(self,image,instanceType,keyName,security_GroupsId):
        self.instances =self.ec2.create_instances(
        Monitoring={
            'Enabled':True
        },
        ImageId=image,
        MinCount=1,
        MaxCount=1,
        InstanceType=instanceType,
        KeyName=keyName,
        SecurityGroupIds=[security_GroupsId,],
        )
    def delete_instance(self,id):
        self.client.terminate_instances(InstanceIds=[id,])
        print(f"Instance {id} was terminated")
    


