

import yaml

def get_config2():
	with open('config2.yaml', encoding='utf-8') as file:
		data = yaml.load(file, Loader=yaml.FullLoader)
	print(f"data:\n{data['prd']['ip']}")

def get_config():
    with open('config.yaml', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    print(f"data:\n{data['sendmail']['smtpserver']}")

def get_config3():
	with open('config3.yaml', 'r', encoding='utf-8') as fp:
		# yml = yaml.load(fp,Loader=yaml.FullLoader)
		data = fp.read()
	yml = yaml.load(data,Loader=yaml.FullLoader)
	prd_ip = yml['prd']['ip']
	prd_paht = yml['prd']['path']
	print('prd_ip: ',prd_ip)
	print('prd_ip: ',prd_paht)

def main():
	# get_config()
	# get_config2()
	get_config3()

if __name__ == '__main__':
    main()