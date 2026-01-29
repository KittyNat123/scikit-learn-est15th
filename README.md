# Scikit-Learn Machine Learning Project 🤖

이 리포지토리는 **Scikit-Learn** 라이브러리를 중심으로 한 다양한 머신러닝 모델링, 데이터 전처리, 앙상블 기법, 그리고 실전 프로젝트 코드를 담고 있습니다.  
기초 학습부터 심화 튜닝(Optuna), 그리고 AutoML(AutoGluon, H2O) 비교 분석까지, 데이터 사이언스 역량 강화를 위한 포괄적인 자료를 제공합니다.

## 📂 프로젝트 구조 및 내용

### 1. 기초 및 데이터 전처리 (Basics & Preprocessing)
- **Scikit-Learn 입문**: `1_sklearn_start.ipynb` - 라이브러리 기본 구조 및 워크플로우 이해
- **전처리 (Preprocessing)**: `4_sklearn_PreProcess.ipynb` - 데이터 스케일링, 인코딩, 결측치 처리
- **특성 공학 (Feature Engineering)**: `8_polynominal_Feature.ipynb` - 다항 특성 생성 및 활용

### 2. 지도 학습 - 분류 & 회귀 (Supervised Learning)
- **모델 선택 및 튜닝**: `2_ModelSelection.ipynb` - 교차 검증(Cross Validation), GridSearch
- **분류 (Classification)**:
  - `3_SVM.ipynb`: Support Vector Machine 심층 분석
  - `5_sklearn_classification.ipynb`: 다양한 분류 알고리즘 비교
- **회귀 (Regression)**:
  - `9_LinearRegressionModel.ipynb`: 선형 회귀 모델링
  - `Plus_*.ipynb`: 선형 회귀 심화 및 실습 예제

### 3. 앙상블 학습 (Ensemble Learning)
- **핵심 기법**: `10_ensemble.ipynb` - Voting, Bagging, Boosting (Random Forest, GBM 등)
- **하이퍼파라미터 최적화**: `11_ensemble_Optuna.ipynb`, `6_classification_Optuna.ipynb` - **Optuna**를 활용한 고성능 튜닝
- **시각화**: `GBM_visualize.ipynb` - Gradient Boosting 모델의 학습 과정 시각화

### 4. 비지도 학습 (Unsupervised Learning)
- **군집화 및 차원축소**: `13_unsupervisedLearning.ipynb` - K-Means, PCA 등

### 5. 실전 프로젝트 (Mini Projects)
- **Titanic 생존자 예측**: 
  - `7_Titanic.ipynb`: 데이터 분석부터 모델링까지 전체 프로세스
  - `colab_titanic-*.ipynb`: 캐글(Kaggle) 입문 및 고득점 전략 가이드
- **지리 데이터 시각화**: `folium_visualization_colored.ipynb` - Folium을 활용한 인터랙티브 지도 시각화

### 6. 🧠 AutoML (Automated Machine Learning)
> **[AutoML 폴더 바로가기](./AutoML)**
- **AutoGluon vs H2O AutoML**: 두 강력한 AutoML 프레임워크의 상세 비교 및 가이드
- 성능, 사용성, 아키텍처 분석 제공

## 🛠 사용 기술 스택

| 구분 | 기술 / 라이브러리 |
|------|-------------------|
| **언어** | ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) |
| **핵심 라이브러리** | Scikit-Learn, Pandas, NumPy |
| **시각화** | Matplotlib, Seaborn, Folium |
| **최적화** | Optuna |
| **AutoML** | AutoGluon, H2O |

## 🚀 시작 가이드

이 프로젝트의 코드는 **Antigravity** 환경에서 가장 잘 실행됩니다.

1. **리포지토리 클론**:
    ```bash
    git clone https://github.com/KittyNat123/scikit-learn-est15th.git
    cd scikit-learn-est15th
    ```

2. **필수 라이브러리 설치**:
    ```bash
    pip install scikit-learn pandas numpy matplotlib seaborn optuna folium
    ```

3. **Antigravity 실행**:
    
    Antigravity를 통해 프로젝트를 열고 노트북 파일을 실행합니다.

---
💡 *이 코드는 데이터 분석 및 머신러닝 학습 목적으로 작성되었습니다.* ✨
