import jqdatasdk
jqdatasdk.auth('17812137093','Sy16241098')
from jqdatasdk.alpha101 import *
import pandas as pd
<<<<<<< HEAD
import numpy as np
import os
from get_trade_date import get_trade_date
#STARTDATE='20160101'
STARTDATE='20160825'
ENDDATE='20170102'
#ENDDATE='20180101'
=======
from get_trade_date import get_trade_date

STARTDATE='20160101'
ENDDATE='20180101'
>>>>>>> 22dcf899ec4c4f7068102860b61c2ab9d660281e
trade_date_list=get_trade_date(STARTDATE,ENDDATE)
#test_date=create_assist_date("2016-01-01","2020-01-05")


<<<<<<< HEAD
#get worldquant 101 alpha:

for i in range(len(trade_date_list)-1):
    a=pd.DataFrame()
    #for j in range(1,82):
    a.insert(0,'alpha_001',alpha_001(trade_date_list[i],'000300.XSHG'))
    a.insert(1,'alpha_002',alpha_002(trade_date_list[i],'000300.XSHG'))
    a.insert(2,'alpha_003',alpha_003(trade_date_list[i],'000300.XSHG'))
    a.insert(3,'alpha_004',alpha_004(trade_date_list[i],'000300.XSHG'))
    a.insert(4,'alpha_005',alpha_005(trade_date_list[i],'000300.XSHG'))
    a.insert(5,'alpha_006',alpha_006(trade_date_list[i],'000300.XSHG'))
    a.insert(6,'alpha_007',alpha_007(trade_date_list[i],'000300.XSHG'))
    a.insert(7,'alpha_008',alpha_008(trade_date_list[i],'000300.XSHG'))
    a.insert(8,'alpha_009',alpha_009(trade_date_list[i],'000300.XSHG'))
    a.insert(9,'alpha_010',alpha_010(trade_date_list[i],'000300.XSHG'))
    a.insert(10,'alpha_011',alpha_011(trade_date_list[i],'000300.XSHG'))
    a.insert(11,'alpha_012',alpha_012(trade_date_list[i],'000300.XSHG'))
    a.insert(12,'alpha_013',alpha_013(trade_date_list[i],'000300.XSHG'))
    a.insert(13,'alpha_014',alpha_014(trade_date_list[i],'000300.XSHG'))
    a.insert(14,'alpha_015',alpha_015(trade_date_list[i],'000300.XSHG'))
    a.insert(15,'alpha_016',alpha_016(trade_date_list[i],'000300.XSHG'))
    a.insert(16,'alpha_017',alpha_017(trade_date_list[i],'000300.XSHG'))
    a.insert(17,'alpha_018',alpha_018(trade_date_list[i],'000300.XSHG'))
    a.insert(18,'alpha_019',alpha_019(trade_date_list[i],'000300.XSHG'))
    a.insert(19,'alpha_020',alpha_020(trade_date_list[i],'000300.XSHG'))
    a.insert(20,'alpha_021',alpha_021(trade_date_list[i],'000300.XSHG'))
    a.insert(21,'alpha_022',alpha_022(trade_date_list[i],'000300.XSHG'))
    a.insert(22,'alpha_023',alpha_023(trade_date_list[i],'000300.XSHG'))
    a.insert(23,'alpha_024',alpha_024(trade_date_list[i],'000300.XSHG'))
    a.insert(24,'alpha_025',alpha_025(trade_date_list[i],'000300.XSHG'))
    a.insert(25,'alpha_026',alpha_026(trade_date_list[i],'000300.XSHG'))
    a.insert(26,'alpha_027',alpha_027(trade_date_list[i],'000300.XSHG'))
    a.insert(27,'alpha_028',alpha_028(trade_date_list[i],'000300.XSHG'))
    a.insert(28,'alpha_029',alpha_029(trade_date_list[i],'000300.XSHG'))
    a.insert(29,'alpha_030',alpha_030(trade_date_list[i],'000300.XSHG'))
    a.insert(30,'alpha_031',alpha_031(trade_date_list[i],'000300.XSHG'))
    a.insert(31,'alpha_032',alpha_032(trade_date_list[i],'000300.XSHG'))
    a.insert(32,'alpha_033',alpha_033(trade_date_list[i],'000300.XSHG'))
    a.insert(33,'alpha_034',alpha_034(trade_date_list[i],'000300.XSHG'))
    a.insert(34,'alpha_035',alpha_035(trade_date_list[i],'000300.XSHG'))
    a.insert(35,'alpha_036',alpha_036(trade_date_list[i],'000300.XSHG'))
    a.insert(36,'alpha_037',alpha_037(trade_date_list[i],'000300.XSHG'))
    a.insert(37,'alpha_038',alpha_038(trade_date_list[i],'000300.XSHG'))
    a.insert(38,'alpha_039',alpha_039(trade_date_list[i],'000300.XSHG'))
    a.insert(39,'alpha_040',alpha_040(trade_date_list[i],'000300.XSHG'))
    a.insert(40,'alpha_041',alpha_041(trade_date_list[i],'000300.XSHG'))
    a.insert(41,'alpha_042',alpha_042(trade_date_list[i],'000300.XSHG'))
    a.insert(42,'alpha_043',alpha_043(trade_date_list[i],'000300.XSHG'))
    a.insert(43,'alpha_044',alpha_044(trade_date_list[i],'000300.XSHG'))
    a.insert(44,'alpha_045',alpha_045(trade_date_list[i],'000300.XSHG'))
    a.insert(45,'alpha_046',alpha_046(trade_date_list[i],'000300.XSHG'))
    a.insert(46,'alpha_047',alpha_047(trade_date_list[i],'000300.XSHG'))
    #a.insert(47,'alpha_048',np.array(zeros(101,1)))#该因子尚未实现
    a.insert(47,'alpha_049',alpha_049(trade_date_list[i],'000300.XSHG'))
    a.insert(48,'alpha_050',alpha_050(trade_date_list[i],'000300.XSHG'))
    a.insert(49,'alpha_051',alpha_051(trade_date_list[i],'000300.XSHG'))
    a.insert(50,'alpha_052',alpha_052(trade_date_list[i],'000300.XSHG'))
    a.insert(51,'alpha_053',alpha_053(trade_date_list[i],'000300.XSHG'))
    a.insert(52,'alpha_054',alpha_054(trade_date_list[i],'000300.XSHG'))
    a.insert(53,'alpha_055',alpha_055(trade_date_list[i],'000300.XSHG'))
    a.insert(54,'alpha_056',alpha_056(trade_date_list[i],'000300.XSHG'))
    a.insert(55,'alpha_057',alpha_057(trade_date_list[i],'000300.XSHG'))
    #a.insert(57,'alpha_058',alpha_058(trade_date_list[i],'000300.XSHG'))
    #a.insert(58,'alpha_059',alpha_059(trade_date_list[i],'000300.XSHG'))
    a.insert(56,'alpha_060',alpha_060(trade_date_list[i],'000300.XSHG'))
    a.insert(57,'alpha_061',alpha_061(trade_date_list[i],'000300.XSHG'))
    a.insert(58,'alpha_062',alpha_062(trade_date_list[i],'000300.XSHG'))
    #a.insert(62,'alpha_063',alpha_063(trade_date_list[i],'000300.XSHG'))
    a.insert(59,'alpha_064',alpha_064(trade_date_list[i],'000300.XSHG'))
    a.insert(60,'alpha_065',alpha_065(trade_date_list[i],'000300.XSHG'))
    a.insert(61,'alpha_066',alpha_066(trade_date_list[i],'000300.XSHG'))
    #a.insert(66,'alpha_067',alpha_067(trade_date_list[i],'000300.XSHG'))
    a.insert(62,'alpha_068',alpha_068(trade_date_list[i],'000300.XSHG'))
    #a.insert(68,'alpha_069',alpha_069(trade_date_list[i],'000300.XSHG'))
    #a.insert(69,'alpha_070',alpha_070(trade_date_list[i],'000300.XSHG'))
    a.insert(63,'alpha_071',alpha_071(trade_date_list[i],'000300.XSHG'))
    a.insert(64,'alpha_072',alpha_072(trade_date_list[i],'000300.XSHG'))
    a.insert(65,'alpha_073',alpha_073(trade_date_list[i],'000300.XSHG'))
    a.insert(66,'alpha_074',alpha_074(trade_date_list[i],'000300.XSHG'))
    a.insert(67,'alpha_075',alpha_075(trade_date_list[i],'000300.XSHG'))
    #a.insert(75,'alpha_076',alpha_076(trade_date_list[i],'000300.XSHG'))
    #a.insert(76,'alpha_077',alpha_077(trade_date_list[i],'000300.XSHG'))
    a.insert(68,'alpha_078',alpha_078(trade_date_list[i],'000300.XSHG'))
    #a.insert(78,'alpha_079',alpha_079(trade_date_list[i],'000300.XSHG'))
    #a.insert(79,'alpha_080',alpha_080(trade_date_list[i],'000300.XSHG'))
    #a.insert(80,'alpha_081',alpha_081(trade_date_list[i],'000300.XSHG'))
    #a.insert(81,'alpha_082',alpha_082(trade_date_list[i],'000300.XSHG'))
    a.insert(69,'alpha_083',alpha_083(trade_date_list[i],'000300.XSHG'))
    a.insert(70,'alpha_084',alpha_084(trade_date_list[i],'000300.XSHG'))
    a.insert(71,'alpha_085',alpha_085(trade_date_list[i],'000300.XSHG'))
    a.insert(72,'alpha_086',alpha_086(trade_date_list[i],'000300.XSHG'))
    #a.insert(86,'alpha_087',alpha_087(trade_date_list[i],'000300.XSHG'))
    a.insert(73,'alpha_088',alpha_088(trade_date_list[i],'000300.XSHG'))
    #a.insert(88,'alpha_089',alpha_089(trade_date_list[i],'000300.XSHG'))
    #a.insert(89,'alpha_090',alpha_090(trade_date_list[i],'000300.XSHG'))
    #a.insert(90,'alpha_091',alpha_091(trade_date_list[i],'000300.XSHG'))
    a.insert(74,'alpha_092',alpha_092(trade_date_list[i],'000300.XSHG'))
    #a.insert(92,'alpha_093',alpha_093(trade_date_list[i],'000300.XSHG'))
    a.insert(75,'alpha_094',alpha_094(trade_date_list[i],'000300.XSHG'))
    a.insert(76,'alpha_095',alpha_095(trade_date_list[i],'000300.XSHG'))
    a.insert(77,'alpha_096',alpha_096(trade_date_list[i],'000300.XSHG'))
    #a.insert(96,'alpha_097',alpha_097(trade_date_list[i],'000300.XSHG'))
    a.insert(78,'alpha_098',alpha_098(trade_date_list[i],'000300.XSHG'))
    a.insert(79,'alpha_099',alpha_099(trade_date_list[i],'000300.XSHG'))
    #a.insert(99,'alpha_100',alpha_100(trade_date_list[i],'000300.XSHG'))
    a.insert(80,'alpha_101',alpha_101(trade_date_list[i],'000300.XSHG'))
    #factor_path=os.path.join("./factor/{}".format(trade_date_list[i])+'.xlsx')
    #/Users/litinglan/Desktop/Investment_Pro/stock_pro/factor
    a.to_csv('/Users/litinglan/Desktop/Investment_Pro/stock_pro/factor/{}'.format(trade_date_list[i])+'.csv')
=======
#get worldquant 101 alpha
for i in range(len(trade_date_list)-1):
    df=pd.DataFrame()
    df.append(alpha_001(trade_date_list[i],'000300.XSHG'))
    pass
#我们从一个dataframe中选取一列series1.
series1=data.pop('day')
#为df1添加一个列，第一个0我们可以改变选择你想插入的位置，第二个可以选择你想要的名字
df.insert(0,'series1',series1)
#对这一列赋值
#df['series1']=series1
>>>>>>> 22dcf899ec4c4f7068102860b61c2ab9d660281e

