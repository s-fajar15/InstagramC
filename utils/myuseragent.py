import random
import os

class DeviceCatalog:
    @staticmethod
    def app_version():
        return [
            {"version": "368.0.0.45.96", "code": "700073482"},
            {"version": "361.0.0.46.88", "code": "674674275"},
            {"version": "309.1.0.41.113", "code": "672461242"}
        ]

    @staticmethod
    def generate_device():
        return {
            'TECNO': [
                {'model': 'TECNO LH8n', 'product': 'TECNO-LH8n', 'hardware': 'mt6789', 'version': '13'},
                {'model': 'TECNO LI7', 'product': 'TECNO-LI7', 'hardware': 'mt6789', 'version': '14'},
                {'model': 'TECNO KJ7s', 'product': 'TECNO-KJ7s', 'hardware': 'mt6789', 'version': '14'},
                {'model': 'TECNO LG8n', 'product': 'TECNO-LG8n', 'hardware': 'mt6789', 'version': '12'},
                {'model': 'TECNO KJ6', 'product': 'TECNO-KJ6', 'hardware': 'mt6789', 'version': '13'},
                {'model': 'TECNO CK7n', 'product': 'TECNO-CK7n', 'hardware': 'mt6789', 'version': '14'},
                {'model': 'TECNO Pova 5', 'product': 'TECNO-Pova5', 'hardware': 'mt6789', 'version': '13'},
                {'model': 'TECNO Spark 20', 'product': 'TECNO-KD7', 'hardware': 'mt6765', 'version': '13'},
                {'model': 'TECNO Camon 30', 'product': 'TECNO-CK8', 'hardware': 'mt6893', 'version': '14'},
                {'model': 'TECNO Phantom X2', 'product': 'TECNO-AD9', 'hardware': 'mt6893', 'version': '13'},
            ],
            'realme': [
                {'model': 'RMX3370', 'product': 'RE879AL1', 'hardware': 'qcom', 'version': '13'},
                {'model': 'RMX3363', 'product': 'RE54ABL1', 'hardware': 'qcom', 'version': '13'},
                {'model': 'RMX3151', 'product': 'RE54B4L1', 'hardware': 'mt6781', 'version': '13'},
                {'model': 'RMX1851', 'product': 'RMX1851', 'hardware': 'qcom', 'version': '10'},
                {'model': 'RMX1971', 'product': 'RMX1971', 'hardware': 'qcom', 'version': '10'},
                {'model': 'RMX3085', 'product': 'realme-8', 'hardware': 'mt6785', 'version': '12'},
                {'model': 'RMX3710', 'product': 'RE9AL1', 'hardware': 'qcom', 'version': '14'},
                {'model': 'RMX3461', 'product': 'RE879BL1', 'hardware': 'mt6893', 'version': '13'},
                {'model': 'RMX3686', 'product': 'RE55AL1', 'hardware': 'qcom', 'version': '14'},
            ],
            'samsung': [
                {'model': 'SM-A135F', 'product': 'a13', 'hardware': 'exynos850', 'version': '14'},
                {'model': 'SM-G998N', 'product': 'p3s', 'hardware': 'exynos2100', 'version': '14'},
                {'model': 'SM-F721N', 'product': 'b4q', 'hardware': 'qcom', 'version': '14'},
                {'model': 'SM-S928U1', 'product': 'e3q', 'hardware': 'qcom', 'version': '14'},
                {'model': 'SM-A515F', 'product': 'a51', 'hardware': 'exynos9611', 'version': '13'},
                {'model': 'SM-N981N', 'product': 'c1q', 'hardware': 'qcom', 'version': '13'},
                {'model': 'SM-F711N', 'product': 'b2q', 'hardware': 'qcom', 'version': '14'},
                {'model': 'SM-M127F', 'product': 'm12', 'hardware': 'exynos850', 'version': '12'},
                {'model': 'SM-A546E', 'product': 'a54x', 'hardware': 'exynos1380', 'version': '14'},
                {'model': 'SM-S921B', 'product': 'dm1q', 'hardware': 'qcom', 'version': '14'},
                {'model': 'SM-A326B', 'product': 'a32x', 'hardware': 'mt6769v', 'version': '13'},
            ],
            'vivo': [
                {'model': 'vivo 2007', 'product': '1906', 'hardware': 'qcom', 'version': '11'},
                {'model': 'vivo 1907', 'product': '1907', 'hardware': 'mt6768', 'version': '12'},
                {'model': 'V2206', 'product': 'V2206', 'hardware': 'qcom', 'version': '12'},
                {'model': 'vivo 1910', 'product': '1910', 'hardware': 'qcom', 'version': '9'},
                {'model': 'vivo Y20', 'product': 'Y20', 'hardware': 'mt6765', 'version': '11'},
                {'model': 'vivo V29', 'product': 'V2250', 'hardware': 'qcom', 'version': '14'},
                {'model': 'vivo Y36', 'product': 'V2247', 'hardware': 'qcom', 'version': '13'},
                {'model': 'vivo Y22', 'product': 'V2207', 'hardware': 'mt6765', 'version': '13'},
                {'model': 'vivo X80', 'product': 'V2183A', 'hardware': 'mt6983', 'version': '13'},
            ],
            'Xiaomi': [
                {'model': 'M2007J3SG', 'product': 'apollo', 'hardware': 'qcom', 'version': '12'},
                {'model': 'M2101K7BNY', 'product': 'rosemary', 'hardware': 'mt6785', 'version': '13'},
                {'model': 'Redmi Note 7', 'product': 'lavender', 'hardware': 'qcom', 'version': '9'},
                {'model': 'Redmi Note 8 Pro', 'product': 'begonia', 'hardware': 'mt6785', 'version': '10'},
                {'model': 'Redmi Note 8', 'product': 'ginkgo', 'hardware': 'qcom', 'version': '9'},
                {'model': 'Poco X3 Pro', 'product': 'vayu', 'hardware': 'qcom', 'version': '12'},
                {'model': 'Redmi Note 10 Pro', 'product': 'sweet', 'hardware': 'qcom', 'version': '13'},
                {'model': 'Redmi Note 12', 'product': 'sunstone', 'hardware': 'mt6789', 'version': '13'},
                {'model': 'Xiaomi 12T Pro', 'product': 'diting', 'hardware': 'qcom', 'version': '14'},
                {'model': 'Redmi Note 13 Pro', 'product': 'garnet', 'hardware': 'mt6893', 'version': '14'},
            ],
            'Infinix': [
                {'model': 'Infinix X680', 'product': 'x680', 'hardware': 'mt6789', 'version': '13'},
                {'model': 'Infinix Note 30', 'product': 'note30', 'hardware': 'mt6893', 'version': '14'},
                {'model': 'Infinix Hot 12', 'product': 'hot12', 'hardware': 'mt6762', 'version': '12'},
                {'model': 'Infinix Zero 5G', 'product': 'zero5g', 'hardware': 'qcom', 'version': '13'},
            ],
            'OPPO': [
                {'model': 'CPH2389', 'product': 'OPPO-A1', 'hardware': 'qcom', 'version': '14'},
                {'model': 'CPH2211', 'product': 'OPPO-Reno', 'hardware': 'mt6893', 'version': '13'},
                {'model': 'OPPO A57', 'product': 'oppoa57', 'hardware': 'mt6765', 'version': '13'},
                {'model': 'OPPO Find X6', 'product': 'findx6', 'hardware': 'qcom', 'version': '14'},
            ],
            'OnePlus': [
                {'model': 'OnePlus9', 'product': 'lemon', 'hardware': 'qcom', 'version': '12'},
                {'model': 'OnePlus 10T', 'product': 'dipper', 'hardware': 'qcom', 'version': '13'},
                {'model': 'OnePlus Nord', 'product': 'nord', 'hardware': 'qcom', 'version': '12'},
                {'model': 'OnePlus 11', 'product': 'borealis', 'hardware': 'qcom', 'version': '14'},
            ]
        }


class UserAgentGenerator:
    def __init__(self):
        self.model = DeviceCatalog.generate_device()
        self.device_list = list(self.model.keys())
        self.dpi_pixel = random.choice([
            '240dpi; 1760x792', '240dpi; 1920x864', '320dpi; 2400x1080',
            '400dpi; 3200x1440', '480dpi; 1080x1920', '320dpi; 900x1600',
            '320dpi; 720x1280', '240dpi; 540x960', '280dpi; 1920x1080',
            '240dpi; 160x900', '240dpi; 1280x720', '160dpi; 960x540'
        ])

    @staticmethod
    def android_version(android_version):
        version_map = {'9': '28', '10': '29', '11': '30', '12': '31', '13': '32', '14': '33'}
        return version_map.get(str(android_version), '34')

    def get_device(self, brand=None, default=False):
        if default:
            brand = os.popen("getprop ro.product.manufacturer").read().strip() or None
            product = os.popen("getprop ro.product.device").read().strip() or None
            model = os.popen("getprop ro.product.model").read().strip() or None
            hardware = os.popen("getprop ro.hardware").read().strip() or None
            version = os.popen("getprop ro.build.version.release").read().strip() or None
            sdk = os.popen("getprop ro.build.version.sdk").read().strip() or None

            if not all([brand, model, sdk]):
                return self.get_device(brand=random.choice(self.device_list))
        else:
            if brand is None or brand not in self.model:
                brand = random.choice(self.device_list)

            device_list = self.model.get(brand, [])
            if not device_list:
                raise ValueError(f"Tidak ada perangkat yang tersedia untuk merek: {brand}")

            device = random.choice(device_list)
            product = device.get('product', '')
            model = device.get('model', '')
            hardware = device.get('hardware', '')
            version = device.get('version', '')
            sdk = self.android_version(device.get('version', ''))

        return {
            'brand': brand,
            'model': model,
            'product': product,
            'hardware': hardware,
            'version': version,
            'sdk': sdk,
        }

    def generate_user_agent(self, brand=None, default=False):
        device_info = self.get_device(brand, default)
        app_version = random.choice(DeviceCatalog.app_version())
        brand, model, product, hardware, version, sdk = device_info.values()
        return (f'Instagram 361.0.0.46.88 Android ({sdk}/{version}; {self.dpi_pixel}; {brand}; {model}; {product}; {hardware}; in_ID; 674674275)')
