

def change_makefile():
    f = open("emq-rel/Makefile", "rb")
    data = f.read()
    f.close()

    if data.find("emq_lwm2m") < 0:
        data = data.replace("emq_auth_pgsql emq_auth_mongo", "emq_auth_pgsql emq_auth_mongo emq_lwm2m\n\ndep_emq_lwm2m = git https://github.com/emq/emq-lwm2m\n\n")
        f = open("emq-rel/Makefile", "wb")
        f.write(data)
        f.close()
        

    f = open("emq-rel/relx.config", "rb")
    data = f.read()
    f.close()

    if data.find("emq_lwm2m") < 0:
        f = open("emq-rel/relx.config", "wb")
        data = data.replace("{emq_auth_mongo, load}", "{emq_auth_mongo, load},\n{emq_lwm2m, load}")
        data = data.replace('{template, "rel/conf/emq.conf", "etc/emq.conf"},', \
                '{template, "rel/conf/emq.conf", "etc/emq.conf"},'+  \
                '\n    {template, "rel/conf/plugins/emq_lwm2m.conf", "etc/plugins/emq_lwm2m.conf"},'+  \
                '\n    {copy, "deps/emq_lwm2m/lwm2m_xml", "etc/"},')
        f.write(data)
        f.close()
        
        
        
def change_lwm2m_config():
    f = open("emq-rel/deps/emq_lwm2m/etc/emq_lwm2m.conf", "rb")
    data = f.read()
    f.close()
    
    if data.find("5783") > 0:
        data = data.replace("5783", "5683")
        f = open("emq-rel/deps/emq_lwm2m/etc/emq_lwm2m.conf", "wb")
        f.write(data)
        f.close()
    
    

def main():
    change_makefile()
    change_lwm2m_config()
    
    
if __name__ == "__main__":
    main()
    
    