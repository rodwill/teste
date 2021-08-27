import random
import time

from locust import HttpUser, task


class QuickstartUser(HttpUser):

    def trunc(self, f, n):
        s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return '.'.join([i, (d + '0' * n)[:n]])

    def on_start(self):
        print('starting...')
    #     f = open('teste.txt', "w+")
    #     for i in range(1000000):
    #         length = random.randrange(1000, 100000)
    #         f.write(str(length))
    #     f.close()
    #     print('fim-on_start')
    #     f = open('teste.txt', "r")
    #     f.seek(0, 2)
    #     tam = f.tell() / 1024 / 1024
    #     print("Tamanho do arquivo sendo enviado: " + self.trunc(tam, 2) + "MB")
    #     f.close()

    @task
    def teste_1(self):
        payload = {}
        # files = [('file', ('cnpj.txt', open('teste.txt', 'rb'), 'application/octet-stream'))]
        # open('teste.txt', 'rb')
        headers = {}
        resp = self.client.get(url='/api/rest/publico/certidoes/16954655000139?seEmitirPDF=true', headers=headers)
        # time.sleep(0.3)
        if resp.status_code != 200:
            print("Erro request")
            print(f'Status Code = {resp.status_code}')
            print(resp.text)
