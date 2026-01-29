import json
import os

# Target file path
file_path = 'Plus_6_LinearRegression.ipynb'

# Check if file exists
if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
    exit(1)

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Visualization code snippet
    # Using 'df' as requested by the user
    # Columns: Longitude, Latitude, Population, MedHouseVal (target)
    source_code = [
        "# 캘리포니아 주택 가격 데이터 지도 시각화\n",
        "# 전제: 'df'라는 이름의 DataFrame이 이미 생성되어 있어야 합니다.\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "df.plot(kind=\"scatter\", x=\"Longitude\", y=\"Latitude\", alpha=0.4,\n",
        "    s=df[\"Population\"]/100, label=\"Population\", figsize=(10,7),\n",
        "    c=\"MedHouseVal\", cmap=plt.get_cmap(\"jet\"), colorbar=True,\n",
        "    sharex=False)\n",
        "plt.legend()\n",
        "plt.show()\n"
    ]

    # Create a new code cell
    new_cell = {
        "cell_type": "code",
        "execution_count": None,
        "id": "visualization_cell",
        "metadata": {},
        "outputs": [],
        "source": source_code
    }

    # Append the new cell to the notebook
    data['cells'].append(new_cell)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1)
    
    print(f"Successfully added visualization code to {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")
