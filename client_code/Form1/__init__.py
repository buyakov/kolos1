from ._anvil_designer import Form1Template
from anvil import *
import anvil.http

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    uchastok = self.drop_down_1.items
    uchastok = 2
    data = ((2, '43:40:032706:2', 877),
            (3, '43:40:032706:3', 635),
            (4, '43:40:032706:4', 649),
            (5, '43:40:032706:5', 837),
            (6, '43:40:032706:6', 990),
            (7, '43:40:032706:7', 395),
            (8, '43:40:032706:8', 416),
            (9, '43:40:032706:9', 836),
            (10, '43:40:032706:10', 432),
            (11, '43:40:032706:11', 429),
            (12, '43:40:032706:12', 779),
            (13, '43:40:032706:13', 554),
            (14, '43:40:032706:14', 529),
            (15, '43:40:032706:15', 660),
            (16, '43:40:032706:16', 839),
            (17, '43:40:032706:17', 365),
            (18, '43:40:032706:18', 386),
            (19, '43:40:032706:19', 421),
            (20, '43:40:032706:20', 404),
            (21, '43:40:032706:21', 492),
            (22, '43:40:032706:22', 457),
            (23, '43:40:032706:23', 369),
            (24, '43:40:032706:24', 411),
            (25, '43:40:032706:25', 369),
            (26, '43:40:032706:26', 380),
            (27, '43:40:032706:27', 395),
            (28, '43:40:032706:28', 409),
            (29, '43:40:032706:29', 691),
            (30, '43:40:032706:30', 542),
            (31, '43:40:032706:31', 432),
            (32, '43:40:032706:32', 398),
            (33, '43:40:032706:33', 400),
            (34, '43:40:032706:34', 413),
            (35, '43:40:032706:35', 406),
            (36, '43:40:032706:36', 399),
            (37, '43:40:032706:37', 418),
            (38, '43:40:032706:38', 439),
            (39, '43:40:032706:39', 360),
            (40, '43:40:032706:40', 378),
            (41, '43:40:032706:41', 381),
            (42, '43:40:032706:42', 397),
            (43, '43:40:032706:43', 398),
            (44, '43:40:032706:44', 405),
            (45, '43:40:032706:45', 408),
            (46, '43:40:032706:46', 438),
            (47, '43:40:032706:47', 702),
            (48, '43:40:032706:48', 469),
            (49, '43:40:032706:49', 418),
            (50, '43:40:032706:50', 401),
            (51, '43:40:032706:51', 773),
            (52, '43:40:032706:52', 381),
            (53, '43:40:032706:53', 372),
            (54, '43:40:032706:54', 379),
            (55, '43:40:032706:55', 373),
            (56, '43:40:032706:56', 372),
            (57, '43:40:032706:57', 449),
            (58, '43:40:032706:58', 391),
            (59, '43:40:032706:59', 403),
            (60, '43:40:032706:60', 394),
            (61, '43:40:032706:61', 398),
            (62, '43:40:032706:62', 408),
            (63, '43:40:032706:63', 384),
            (64, '43:40:032706:64', 399),
            (65, '43:40:032706:65', 908),
            (66, '43:40:032706:66', 537),
            (67, '43:40:032706:67', 887),
            (68, '43:40:032706:68', 426),
            (69, '43:40:032706:69', 390),
            (70, '43:40:032706:70', 388),
            (71, '43:40:032706:71', 370),
            (72, '43:40:032706:72', 396),
            (73, '43:40:032706:73', 397),
            (74, '43:40:032706:74', 379),
            (75, '43:40:032706:75', 497),
            (76, '43:40:032706:76', 661),
            (77, '43:40:032706:77', 411),
            (78, '43:40:032706:78', 571),
            (79, '43:40:032706:79', 432),
            (80, '43:40:032706:80', 402),
            (81, '43:40:032706:81', 576),
            (82, '43:40:032706:82', 495),
            (83, '43:40:032706:83', 1068),
            (84, '43:40:032706:84', 389),
            (85, '43:40:032706:85', 411),
            (86, '43:40:032706:86', 401),
            (87, '43:40:032706:87', 463),
            (88, '43:40:032706:88', 700),
            (89, '43:40:032706:89', 393),
            (90, '43:40:032706:90', 815),
            (91, '43:40:032706:91', 818),
            (92, '43:40:032706:92', 398),
            (93, '43:40:032706:93', 475),
            (94, '43:40:032706:94', 436),
            (95, '43:40:032706:95', 811),
            (96, '43:40:032706:96', 419),
            (97, '43:40:032706:97', 369),
            (98, '43:40:032706:98', 397),
            (99, '43:40:032706:99', 396),
            (100, '43:40:032706:100', 717),
            (101, '43:40:032706:101', 489),
            (102, '43:40:032706:102', 606),
            (103, '43:40:032706:103', 699),
            (104, '43:40:032706:104', 565),
            (105, '43:40:032706:105', 684),
            (106, '43:40:032706:106', 1169),
            (107, '43:40:032706:107', 853),
            (108, '43:40:032706:108', 520),
            (109, '43:40:032706:109', 497),
            (110, '43:40:032706:110', 774),
            (111, '43:40:032706:111', 651),
            (112, '43:40:032706:112', 492),
            (113, '43:40:032706:113', 955),
            (114, '43:40:032706:114', 1243),
            (115, '43:40:032706:115', 1203),
            (116, '43:40:032706:116', 1037),
            (117, '43:40:032706:117', 516),
            (118, '43:40:032706:118', 783),
            (119, '43:40:032706:119', 753),
            (120, '43:40:032706:120', 857),
            (121, '43:40:032706:121', 852),
            (122, '43:40:032706:122', 790),
            (123, '43:40:032706:123', 695),
            (124, '43:40:032706:124', 862),
            (125, '43:40:032706:125', 771),
            (126, '43:40:032706:126', 934),
            (127, '43:40:032706:127', 1661),
            (128, '43:40:032706:128', 872),
            (129, '43:40:032706:129', 866),
            (130, '43:40:032706:130', 790),
            (131, '43:40:032706:131', 844),
            (132, '43:40:032706:132', 828),
            (133, '43:40:032706:133', 837),
            (134, '43:40:032706:134', 753),
            (135, '43:40:032706:135', 830),
            (136, '43:40:032706:136', 833),
            (137, '43:40:032706:137', 812),
            (138, '43:40:032706:138', 788),
            (139, '43:40:032706:139', 513),
            (140, '43:40:032706:140', 405),
            (141, '43:40:032706:141', 826),
            (142, '43:40:032706:142', 671),
            (143, '43:40:032706:143', 868),
            (144, '43:40:032706:144', 743),
            (145, '43:40:032706:145', 800),
            (146, '43:40:032706:146', 748),
            (147, '43:40:032706:147', 755),
            (148, '43:40:032706:148', 703),
            (149, '43:40:032706:149', 756),
            (150, '43:40:032706:150', 743),
            (151, '43:40:032706:151', 785),
            (152, '43:40:032706:152', 843),
            (153, '43:40:032706:153', 823),
            (154, '43:40:032706:154', 1528),
            (155, '43:40:032706:155', 766),
            (156, '43:40:032706:156', 783),
            (157, '43:40:032706:157', 782),
            (158, '43:40:032706:158', 760),
            (159, '43:40:032706:159', 745),
            (170, '43:40:052706:8', 929),
            (171, '43:40:052706:7', 940),
            (172, '43:40:052706:6', 1042),
            (173, '43:40:052706:5', 1078),
            (174, '43:40:052706:4', 1088),
            (175, '43:40:052706:3', 1078),
            (176, '43:40:052706:2', 1123))
    num = list(filter(lambda x: x[0] == uchastok, data))[0][0]
    sq = list(filter(lambda x: x[0] == uchastok, data))[0][2]
    link = anvil.http.url_decode('https://www.bcgen.com/demo/IDAutomationStreamingQRCode.aspx?ECL=L&D=ST00012|Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО ""КОЛОС-1""|PersonalAcc=40703810400130000655|BankName=АО КБ ""ХЛЫНОВ"", Г.КИРОВ|BIC=043304711|CorrespAcc=30101810100000000711|PayeeINN=4346026874|KPP=434501001|Purpose=ЧЛ/ЦЕЛ ВЗНОС, УЧАСТОК №' + str(num) + '|Sum=' + str(sq*100+100000) + '&MODE=B&PT=T&X=0.1&O=0&LM=0.2&V=0')
    self.image_1.source = link
    pass