# Generated by Django 2.1.10 on 2019-11-17 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=50, unique=True, verbose_name='索引网址')),
                ('content', models.TextField(verbose_name='网页内容')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '网页内容',
                'verbose_name_plural': '网页内容',
                'db_table': 'Content',
            },
        ),
        migrations.CreateModel(
            name='Cpu_Min',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('cpu', models.CharField(max_length=15, verbose_name='CPU使用率')),
                ('menory', models.CharField(max_length=15, verbose_name='内存使用率')),
                ('network_send', models.CharField(max_length=20, verbose_name='上传流量Mb/小时')),
                ('network_recv', models.CharField(max_length=20, verbose_name='接收流量Mb/小时')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '资源消耗',
                'verbose_name_plural': '资源消耗',
                'db_table': 'Cpu_Min',
            },
        ),
        migrations.CreateModel(
            name='Domains',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=30, unique=True, verbose_name='域名')),
                ('BA_sex', models.CharField(default='企业', max_length=50, verbose_name='性质')),
                ('BA_name', models.CharField(max_length=50, verbose_name='名称')),
                ('BA_id', models.CharField(max_length=50, verbose_name='编号')),
                ('counts', models.CharField(default=0, max_length=8, verbose_name='捕获数量')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '监控域名',
                'verbose_name_plural': '监控域名',
                'db_table': 'Domains',
            },
        ),
        migrations.CreateModel(
            name='Error_Log',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100, verbose_name='异常网址')),
                ('error', models.TextField(verbose_name='报错内容')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '错误日志',
                'verbose_name_plural': '错误日志',
                'db_table': 'Error_Log',
            },
        ),
        migrations.CreateModel(
            name='IP',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=15, unique=True, verbose_name='IP地址')),
                ('servers', models.TextField(verbose_name='端口服务')),
                ('host_type', models.CharField(max_length=10, verbose_name='操作系统')),
                ('alive_urls', models.TextField(verbose_name='部署网站')),
                ('area', models.CharField(max_length=400, verbose_name='IP归属')),
                ('cs', models.CharField(default='暂无信息', max_length=20, verbose_name='隶属C段')),
                ('get', models.CharField(default='否', max_length=1, verbose_name='是否校验')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '主机端口',
                'verbose_name_plural': '主机端口',
                'db_table': 'IP',
            },
        ),
        migrations.CreateModel(
            name='Other_Url',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100, unique=True, verbose_name='爬行网址')),
                ('title', models.CharField(default='None', max_length=220, verbose_name='网站标题')),
                ('power', models.CharField(default='None', max_length=200, verbose_name='容器/语言')),
                ('server', models.CharField(default='None', max_length=100, verbose_name='服务器类型')),
                ('status', models.CharField(default='None', max_length=4, verbose_name='请求响应')),
                ('ip', models.CharField(max_length=15, verbose_name='IP地址')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '网络资产',
                'verbose_name_plural': '网络资产',
                'db_table': 'Other_Url',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='萌萌哒屎壳郎一号方案', max_length=30, verbose_name='配置方案')),
                ('Alive_Code', models.CharField(default='[200,204,206,301,302,304,401,402,403,404,500,501,502,503]', max_length=250, verbose_name='允许入库状态码')),
                ('Thread', models.CharField(default='2', max_length=4, verbose_name='线程数量')),
                ('Pool', models.CharField(default='4', max_length=4, verbose_name='线程池量')),
                ('processes', models.CharField(default='4', max_length=4, verbose_name='进程数量')),
                ('childconcurrency', models.CharField(default='8', max_length=4, verbose_name='子协程数量')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '配置信息',
                'verbose_name_plural': '配置信息',
                'db_table': 'Setting',
            },
        ),
        migrations.CreateModel(
            name='Show_Data',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=50, unique=True, verbose_name='展示网址')),
                ('title', models.CharField(default='None', max_length=200, verbose_name='网站标题')),
                ('power', models.CharField(default='None', max_length=150, verbose_name='容器/语言')),
                ('server', models.CharField(default='None', max_length=150, verbose_name='服务器类型')),
                ('status', models.CharField(default='None', max_length=4, verbose_name='请求响应')),
                ('ip', models.CharField(max_length=15, verbose_name='IP地址')),
                ('cs', models.CharField(default='暂无信息', max_length=20, verbose_name='隶属C段')),
                ('servers', models.TextField(default='None', verbose_name='端口服务')),
                ('alive_urls', models.TextField(default='None', verbose_name='部署网站')),
                ('host_type', models.CharField(default='None', max_length=10, verbose_name='操作系统')),
                ('area', models.CharField(default='None', max_length=400, verbose_name='IP归属')),
                ('belong_domain', models.CharField(db_index=True, default='None', max_length=15, verbose_name='所属域名')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('success', models.CharField(default='否', max_length=1, verbose_name='监控齐全')),
                ('check', models.CharField(default='否', max_length=1, verbose_name='是否检测')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Content', verbose_name='网页内容')),
            ],
            options={
                'verbose_name': '数据展示',
                'verbose_name_plural': '数据展示',
                'db_table': 'Show_Data',
            },
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=50, unique=True, verbose_name='索引网址')),
                ('get', models.CharField(default='否', max_length=1, verbose_name='是否爬行')),
                ('ip', models.CharField(max_length=15, verbose_name='IP地址')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '网址索引',
                'verbose_name_plural': '网址索引',
                'db_table': 'URL',
            },
        ),
    ]
