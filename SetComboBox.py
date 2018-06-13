import urllib.request
import xml.etree.ElementTree as ET
from PyQt5.QtGui import QPixmap
import Navermap



def CompanySettingFunc(sigunCode,  CompanyBox):

    nameList = []

    if sigunCode == 0:
        url = 'https://openapi.gg.go.kr/GameSoftwaresManufacture?KEY=48e44bb7e8394490a2ce2f490628ab1b&pIndex=1&pSize=1000'
    else:
        url = 'https://openapi.gg.go.kr/GameSoftwaresManufacture?KEY=48e44bb7e8394490a2ce2f490628ab1b&pIndex=1&pSize=1000' + '&SIGUN_CD=' + str(sigunCode)


    url2 = urllib.request.urlopen(url).read()
    url2 = url2.decode("UTF-8")
    et = ET.fromstring(str(url2))
    iter = et.getiterator("row")

    for i in iter:
        name = i.find("BIZPLC_NM")


        nameList.append(name.text)


    for i in nameList:
        CompanyBox.addItem(str(i), str(i))


    nameList.clear()


def InformationSettingFunc(sigunCode, company, lineEditZipcode,lineEditAddress,  lineEditStatus,  lineEditProduct, lineEditDate,lineEditName , MapView):

    if sigunCode == 0:
        url = 'https://openapi.gg.go.kr/GameSoftwaresManufacture?KEY=48e44bb7e8394490a2ce2f490628ab1b&pIndex=1&pSize=1000'
    else:
        url = 'https://openapi.gg.go.kr/GameSoftwaresManufacture?KEY=48e44bb7e8394490a2ce2f490628ab1b&pIndex=1&pSize=1000' + '&SIGUN_CD=' + str(sigunCode)

    url2 = urllib.request.urlopen(url).read()
    url2 = url2.decode("UTF-8")
    et = ET.fromstring(str(url2))
    iter = et.getiterator("row")

    zipcode = ''
    address = ''
    product = ''
    name = ''
    date = ''
    status = ''
    map_url = ''
    for i in iter:
        if company == i.findtext("BIZPLC_NM"):
            address = i.findtext("REFINE_LOTNO_ADDR")
            status = i.findtext("BSN_STATE_NM")
            product = i.findtext("MANUFACT_TRTMNT_PRODLST_CONT")
            name = i.findtext("BIZPLC_NM")
            date = i.findtext("LICENSG_DE")
            zipcode = i.findtext("REFINE_ZIP_CD")
            x_point = i.findtext("REFINE_WGS84_LOGT")
            y_point = i.findtext("REFINE_WGS84_LAT")
            map_url = Navermap.Set_map_point(x_point, y_point)
            break

    lineEditZipcode.setText(str(zipcode))
    lineEditAddress.setText(str(address))
    lineEditStatus.setText(str(status))
    lineEditProduct.setText(str(product))
    lineEditDate.setText(str(date))
    lineEditName.setText(str(name))



    map_data = urllib.request.urlopen(map_url).read()
    map = QPixmap()
    map.loadFromData(map_data)
    MapView.setPixmap(map)
