
InitNemu(session='srsantos001', workspace='/autofs/unitytravail/travail/srsantos001/PFE', hdcopy=False)

# VM Configurations
VHostConf('debian', enable_kvm=None,  k='fr', m='4G')
VHostConf('android', enable_kvm=None, k='fr', m='4G', boot='d', cdrom='android.iso')

# Debian VM for testing/Wireshark
VHost('test', conf='debian', hds=[VFs('debian10.img', 'cow', tag='test.img')], nics=[VNic(hw='0a:0a:0a:00:01:01'),VNic(hw='0a:0a:0a:00:01:02'), VNic(hw='0c:0c:0c:00:01:01')])

# Android VM
VHost('client', conf='android',hds=[VFs('androidx86_hda.img', 'cow', tag='client.img')])


StartNemu()
