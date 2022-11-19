### pyinstaller

#####1 安装pyinstaller
```shell script
pip install pyinstaller
```

#####2 pyinstaller参数意义

- -F 或者 --onefile

打包单个文件，即项目只有一个文件时使用，项目有多个文件时不要使用
```shell script
pyinstaller -F xxx.py
pyinstaller --onefile xxx.py
```

- -D 或者 --one

打包多个文件，用于框架编写的代码打包
```shell script
pyinstaller -D xxx.py #xxx为项目入口文件
pyinstaller --onedir xxx.py #xxx为项目入口文件
```

- -key=keys

使用keys进行加密打包
```shell script
pyinstalller --key=123 -F xxx.py
```

- -w 或者--windowed 或者--noconsole

表示去掉控制台窗口，使用Windows子系统执行，当程序启动的时候不会打开命令行（只对Windows有效）
```shell script
pyinstaller -w xxx.py
pyinstaller xxx.py --noconsole
```

- -c 或者 --nowindowed 或者 --console

表示打开控制台窗口，使用控制台子系统执行，当程序启动的时候会打开命令行（默认）（只对Windowds有效）
```shell script
pyinstaller -c xxx.py
pyinstaller xxx.py --console
```

- -i 或者 --icon=<file.ioc>

将file.ico添加为可执行文件的资源，改变程序的图标（只对Windows系统有效）
```shell script
pyinstaller -F -i file.ico xxx.py
pyinstall -F --icon=<file.ioc> xxx.py
```
