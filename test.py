
# 检测TVTK是否安装成功
from tvtk.tools import tvtk_doc
# 会自动打开TVTK文档查看工具
# tvtk_doc.main()


# 导入TVTK库
from tvtk.api import tvtk
# 建立一个长方体数据源
s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
print(s)