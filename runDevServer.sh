


# 如果不能运行脚本文件，请chmod +x ./runDevServer.sh  使脚本具有执行权限
# http://127.0.0.1:50001/

serverPort=50002


echo "常见超级用户提示：python manage.py  createsuperuser"

echo "Run XJPython server begin ...."
echo "Run XJPython server : port "  ${serverPort}


python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:${serverPort}



