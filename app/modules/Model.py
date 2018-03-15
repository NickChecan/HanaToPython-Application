import pyhdb
from config import Hana


class Model(object):

    connection = None

    def __init__(self):
        self.connection = pyhdb.connect(Hana.HOST, Hana.PORT, Hana.USER, Hana.PASS)

    @property
    def get_regions(self):
        regions_data = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM \"SALES_TUTORIAL\".\"HanaService.CDSScripts::SalesDDL.Region\"")
        result_set = cursor.fetchall()
        for result in result_set:
            regions_data.append({"regionId": result[0],
                                 "regionName": result[1],
                                 "subRegionName": str(result[2])})
        return regions_data

    @property
    def get_products(self):
        products_data = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM \"SALES_TUTORIAL\".\"HanaService.CDSScripts::SalesDDL.Product\"")
        result_set = cursor.fetchall()
        for result in result_set:
            products_data.append({"productId": result[0],
                                  "productName": result[1]})
        return products_data

    @property
    def get_sales_data(self):
        sales_data = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM \"_SYS_BIC\".\"HanaService/SalesData\"")
        result_set = cursor.fetchall()
        for result in result_set:
            sales_data.append({"regionName": result[0],
                               "productName": result[1],
                               "salesAmount": str(result[2])})
        return sales_data

