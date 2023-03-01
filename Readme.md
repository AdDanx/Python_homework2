Проект собирает ноутбуки с сайтов notik.ru и citilink.ru

Для успешной работы, необходимо наличие браузера Chrome версии 110 либо необходима замена драйвера chromedriver на драйвер для соответствующей версии браузера.

Требуется поставить модули из файла requirements.txt
Требуется установка scrapy по инструкции(https://docs.scrapy.org/en/latest/intro/install.html)

Скрипт выполняется из директории HW2/spiders командой "python 3.10 start_spiders.py"
После выполнения скрипта в директории spiders появляется файл laptops.db

Райтинг ноутбуков рассчитывается на основании весов (int(item['item_mhz'])*(0.01))+int(item['price_rub'])*(-0.01)+int(item['ram']*3)+int(item['ssd'])*0.01)

0.01 для частоты процессора
-0.01 для цены
3 для RAM
0.01 для SSD

По результатам рассчёта рейтинга, в ТОП-5 вошли

1. MSI Creator Z17 A12UHST-258RU i9-12900H 64Gb SSD 2Tb NVIDIA RTX 3080Ti для ноутбуков 16Gb 17 QHD+ TS IPS Cam 90Вт*ч Win11 Серый 9S7-17N112-258
2. MSI CreatorPro Z16P B12UMST-223RU i9-12900H 64Gb SSD 2Tb NVIDIA RTX A5500 для ноутбуков 16Gb 16 QHD+ TS IPS Cam 90Вт*ч Win11Pro Серый 9S7-15G121-223
3. Lenovo ThinkPad E14 Gen 4 Ryzen 7 5825U 40Gb SSD 1Tb AMD Radeon Graphics 14 FHD IPS Cam 57Вт*ч No OS Черный 21EB006PRT
4. Nerpa Caspica I752-15 i7-1255U 32Gb SSD 512Gb Intel Iris Xe Graphics eligible 15,6 FHD IPS Cam 49Вт*ч No OS Серый I752-15AD325100G
5. MAIBENBEN X558 Ryzen 7 5800H 32Gb SSD 1Tb NVIDIA RTX 3060 для ноутбуков 6Gb 15,6 FHD IPS Cam 46,74Вт*ч Linux Серый X558FSJCLGRE0
