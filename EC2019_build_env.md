# 1.環境の用意
WSL（Ubuntu）を入れてから...
```sh
sudo apt update
sudo apt install python
sudo apt install virtualenv
cd ~
mkdir EC2019
cd EC2019
virtualenv -p python2.7 jpnsecCompetition2019
source jpnsecCompetition2019/bin/activate
pip install numpy scipy==0.17.1 algopy matplotlib pandas
sudo apt install gfortran gcc python-dev python-tk git swig liblapack-dev
```
# 2.OpenMDAO
```sh
wget http://openmdao.org/releases/0.10.3.2/go-openmdao-0.10.3.2.py
python go-openmdao-0.10.3.2.py
```
# 3.WISDEM 各種のインストール
```sh
mkdir wisdem
cd wisdem
git clone https://github.com/WISDEM/akima.git
cd akima
git checkout 65c7c9be2b09170befe769bc26c0de2792139ad8
python setup.py develop
cd ../
git clone https://github.com/WISDEM/AirfoilPreppy.git
cd AirfoilPreppy
git checkout 875093ed28ff418f22e1daba952472c932f9eb0d
python setup.py develop
cd ../
git clone https://github.com/WISDEM/CCBlade.git
cd CCBlade
git checkout 9654caa9c256dffa1984c09c8c67e6d0849123c3
python setup.py develop
cd ../
git clone https://github.com/WISDEM/CommonSE.git
cd CommonSE
git checkout bb573cdc1be7a064c03ac446eb409ca683967657
python setup.py develop
cd ../
git clone https://github.com/WISDEM/DriveSE.git
cd DriveSE
git checkout f4f69c2fdb035e11f297e57ba9ac21556c5b11ec
python setup.py develop
cd ../
git clone https://github.com/WISDEM/FloatingSE.git
cd FloatingSE
git checkout f13e0f38a7742ea00a8f446a9ebf505dcf7acd42
python setup.py develop
cd ../
git clone https://github.com/WISDEM/OffshoreBOS.git
cd OffshoreBOS
git checkout 8a5068fcee5e79785c50265d4dbb6d8c1fe801bf
python setup.py develop
cd ../
git clone https://github.com/WISDEM/Plant_FinanceSE.git
cd Plant_FinanceSE
git checkout 8832c7b391e10fe9fc6a9139ea7e5fa17bb0d41f
python setup.py develop
cd ../
git clone https://github.com/WISDEM/RotorSE.git
cd RotorSE
git checkout f044cc78f07cc5a8bafa8e5eadbf43faa70d9293
python setup.py build_ext --inplace
python setup.py develop
cd ../
git clone https://github.com/WISDEM/TowerSE.git
cd TowerSE
git checkout b12faec307a3e08b9a3ef251a93ca4e43036f4b4
python setup.py develop
cd ../
git clone https://github.com/WISDEM/Turbine_CostsSE.git
cd Turbine_CostsSE
git checkout bfbb9f46340635cf5bcf38f4852f2f0e05b55153
python setup.py develop
cd ../
git clone https://github.com/WISDEM/NREL_CSM.git
cd NREL_CSM
git checkout 94efc65a18659976f537b2c64ba126c36113ddf9
python setup.py develop
cd ../
git clone https://github.com/mdolab/pyoptsparse.git
cd pyoptsparse
git checkout c7c1f5af3814bc481303ffed980f4c3ad6be10a1
python setup.py install
cd ../
git clone https://github.com/WISDEM/WISDEM.git
cd WISDEM
git checkout aa3d679928aa5a93618cb8a60d5827db47ba6e76
python setup.py develop
cd ../
git clone https://github.com/WISDEM/pBeam.git
cd pBeam
git checkout 6e8d5169699da5c129d6728b0dd5207a53f07d53
python setup.py develop
cd ../
git clone https://github.com/WISDEM/pyFrame3DD.git
cd pyFrame3DD
git checkout 680a8ba1b00b45ad6f76a76374f2b83cfb3c56df
python setup.py develop
cd ../
git clone https://github.com/WISDEM/pyMAP.git
cd pyMAP
git checkout d63dd3882dcfb3d2d3b89bde56ba19d6fc88cb10
python setup.py develop
cd ../
git clone https://github.com/WISDEM/DriveWPACT.git
cd DriveWPACT
git checkout d872163b9929ce54d7cec3814c3101809d2201b4
python setup.py develop
cd ../
git clone https://github.com/WISDEM/Plant_CostsSE.git
cd Plant_CostsSE
git checkout c93c99fbb23a92c7222f15259bd3e204fb323407
python setup.py develop
cd ../
git clone https://github.com/WISDEM/Plant_EnergySE.git
cd Plant_EnergySE
git checkout 5ca898bf65b63fd1a87a40241591866f5f0b185a
python setup.py develop
cd ../
```
# 4. Fusedwind install
```sh
cd ~/EC2019
git clone https://github.com/FUSED-Wind/fusedwind.git
cd fusedwind
python setup.py develop
cd ../
```
# 5. ダミーパッケージのインストール
```sh
cd ~/EC2019
wget http://www.jpnsec.org/files/competition2019/data/dummies.zip
sudo apt install unzip
unzip dummies.zip
cd dummies
python setup.py install
cd ../
```
# 6. インストールのテスト
```sh
python ~/EC2019/wisdem/WISDEM/src/wisdem/lcoe/lcoe_se_assembly.py
```

# 好きなところに移動させる
```sh
cp -r ~/EC2019 /mnt/c/Users/hogehoge/Desktop/...
```