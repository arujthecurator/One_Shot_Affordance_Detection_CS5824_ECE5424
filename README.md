<!-- - 👋 Hi, I’m @arujthecurator
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ... -->

<!---
arujthecurator/arujthecurator is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

PyTorch implementation of One Shot Affordance Detection, completed as a part of the semester
long project for the course Advanced Machine Learning (CS5824/ECE5424) at Virginia Tech (Fall-2022).

## We have conducted our study by extending the work done in the following papers <a name="1"></a>
* One-Shot Affordance Detection (IJCAI2021) ([link](https://arxiv.org/abs/2106.14747))
> Authors:
> Hongchen Luo, Wei Zhai, Jing Zhang, Yang Cao, Dacheng Tao
* One-Shot Affordance Detection in the Wild (IJCV) ([link](http://arxiv.org/abs/2108.03658))
> Authors:
> Wei Zhai*, Hongchen Luo*, Jing Zhang, Yang Cao, Dacheng Tao

## Requirements <a name="5"></a> 
  - python 3.7 
  - pytorch 1.1.0
  - opencv
  - scipy
  - matplotlib

### Download the Dataset <a name="41"></a> 
- You can download the PAD from [ [Google Drive](https://drive.google.com/file/d/1uKpyIv6rq_R8G2M2ALj6zRe0otkFthPN/view?usp=sharing) | [Baidu Pan](https://pan.baidu.com/s/11lEf4Y05jES2ntb4aS8QaQ) (z40m) ].
- Create a `datasets` folder, and unzip the PAD dataset there.

### Train <a name="61"></a> 
You have to download the pretrained resnet50 model from [ [Google Drive](https://drive.google.com/file/d/16OYi8kAxHosfCo8E4gmFIhwemW1FaCEB/view?usp=sharing) | [Baidu Pan](https://pan.baidu.com/s/1HbsvNctWd6XLXFcbIoq1ZQ) (xjk5) ], 
then move it to the newly created `models` folder. Create `save_models` folder in the OSAD 
directory before training the model. Remember that in the OSAD directory os_ad_1.py, os_ad_2.py, and os_ad_3.py are three different models trained by us. Whichever model you want to train, just rename that model as os_ad.py.
To train the models, execute run_os_ad.py script using the following command:
```bash  
python run_os_ad.py   
```

### Test <a name="62"></a> 
To test these models, execute `run_os_ad.py` script. Make sure in the save_models folder created
before training the models, you are able to see model weights after each epoch:
```bash  
python run_os_ad.py  --mode test 
```
### Evaluation <a name="63"></a> 
In order to evaluate the results, go to the PyMetrics directory and run the requirements.txt
file first by using the bash command:
```bash  
pip install -r requirements.txt
```
Then go to the code folder and execute the test_metrics_3.py script:
```bash  
python test_metrics_3.py
```
## We have referred to the following public github repositories for reference <a name="1"></a>
* One-Shot Affordance Detection (IJCAI2021) ([link](https://github.com/lhc1224/OSAD_Net/tree/def9f6f67e4e3ba2c864a4fcd775e3e80a32f4f8#1))
* One-Shot Affordance Detection Evaluation ([link](https://github.com/lhc1224/OSAD_Net/tree/main/PyMetrics))

## Contributors <a name="9"></a> 
* Aruj Nayak [aruj@vt.edu](aruj@vt.edu).
* Trisha Bora [trishab@vt.edu](trishab@vt.edu).
* Sandeep Chinnareddy [sandeepc98@vt.edu](sandeepc98@vt.edu).
* Akhilesh Marathe [akhimarathe@vt.edu](akhimarathe@vt.edu).
* Prayati Dutta [dprayati@vt.edu](dprayati@vt.edu).



