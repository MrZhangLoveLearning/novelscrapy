#!/bin/bash
echo "run the spider"

base_dir=~/novelscrapy


if [ ! -f $base_dir/env/bin/activate ]
then
	virtualenv $base_dir/env
	
fi


source  $base_dir/env/bin/activate
$base_dir/env/bin/pip install -r $base_dir/requirements.txt
# download the scrapy rely on class
# sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev
# sudo easy_install green let
# sudo easy_install gevent
cd $base_dir/novelscrapy
# scrapy crawl perfect_world
# scrapy crawl beat_god
# scrapy crawl night_king
# scrapy crawl swod_dynasty
python $base_dir/novelscrapy/run.py
