# bit-srun-cli
北理工校园网登录客户端

## 软件特点
* 简单易用，python3编写。
* 可在IPv6网络环境下通过清华源安装。

## 安装步骤

```shell
sudo apt install python3-pip  #安装pip3

pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple srun-bit #通过 -i 指定源
```

## 使用方法

```shell
$ srun-bit
Usage: srun-bit [OPTIONS] COMMAND [ARGS]...

  北理工校园网登录命令行工具

  项目地址 https://github.com/fangli-li/bit-srun-cli

Options:
  --help  Show this message and exit.

Commands:
  config  配置用户名密码
  info    查看网络状态
  login   登录校园网
  logout  注销校园网
```

1. 初次使用 ，先运行 srun-bit config 进行用户名密码配置
2. 使用 srun-bit login 进行登录认证
3. 使用 srun-bit logout 进行认证注销

## 感谢
https://github.com/coffeehat/BIT-srun-login-script