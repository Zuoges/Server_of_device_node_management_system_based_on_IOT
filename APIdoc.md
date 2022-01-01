# 接口文档
## 服务器与设备端通讯用Json消息格式  
```
{
    //设备编号
    "uuid": 0,
    //设备位置
    "local": "415",
    //设备状态 0：断电，1：通电，-1：异常
    "state": 0,
    //用户信息 无用户为NULL
    "user": {
        "name": "Zuoge",
        "id": "A100000"
    },
    //电压
    "vlotage": 220.00,
    //电流
    "current": 1.00,
    //有功功率
    "apower": 220.00,
    //有功电能
    "aelectricity": 1.00,
    //功率因数
    "powerfactor": 1.00,
    //设备状态
    "analysis": {
        "charger": "on",
        "soldering": "up",
        "powersupply": "off"
    }
}
```
## 服务器数据库数据表格式  
|uuid|local|state|vlotage|current|apower|aelectricity|powerfactor|analysis|username|userid|
|---|---|---|---|---|---|---|---|---|---|---|
|0|415|0|220.00|1.00|220.00|1.00|1.00|{"charger": "on","soldering": "up","powersupply": "off"}|Zuoge|A100000|
|...|
## 待补
