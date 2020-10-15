mkdir -pv /etc/portage/patches/dev-libs/pigpio-70
cd /etc/portage/patches/dev-libs/pigpio-70


wget https://github.com/joan2937/pigpio/commit/55d8b880fca26ccf4b897bca1fe66796b9972345.patch -O 02-fix-net-comms-on-arm64.patch
wget https://github.com/joan2937/pigpio/commit/5847d5c0991ba3d8b00fe11125aca5f74f72bc9d.patch -O 01-add-rpi4-arm64-support.patch

cd
emerge -v pigpio