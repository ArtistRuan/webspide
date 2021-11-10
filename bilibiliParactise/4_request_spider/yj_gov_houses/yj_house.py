
import yaml

if __name__ == '__main__':
    with open('config.yaml', encoding='utf-8') as fp:
        yml_data = fp.read()
        print(yml_data)
        print('-------------')
        data = yaml.load(yml_data,Loader=yaml.FullLoader)
        print(data['prd']['proxies_method'])
        print(data['prd']['proxies_ip'])
        print(data['prd']['proxies_port'])

        proxies = {data['prd']['proxies_method']:data['prd']['proxies_ip'] + ':' + data['prd']['proxies_port']}
        print('代理是：',proxies)

