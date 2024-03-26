# Receipt Whisperer

Receipt Whisperer is an innovative solution at the nexus of technology and finance, simplifying the tedious task of inputting receipt information. Through advanced Optical Character Recognition (OCR) technology, it automates text extraction from receipt images. But its capabilities extend beyond mere digitization. The extracted text undergoes thorough processing to identify key details like company name, date, time, receipt number, total amount, and tax.

![Receipt Whisperer Demo](https://github.com/msinacimen/receipt-whisperer/blob/main/receipt_whisperer.gif)

## Getting Started

These instructions will guide you through setting up the project on your local machine.

### Prerequisites

- Anaconda or Miniconda (for managing Python environments)
- Google Vision API key (JSON format)
- Git (for cloning the repository)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/msinacimen/receipt-whisperer.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd receipt-whisperer
   ```

3. **Create and Activate the Conda Environment:**
   ```bash
   conda env create -f GUIenv.yml -n receipt-whisperer
   conda activate receipt-whisperer
   ```

4. **Place your Google Vision API Key:**
   - You also need a key, obtain your `key.json` file from Google Vision API.
   - Place the `key.json` file in the project directory.

### Usage

#### Running the Graphical User Interface (GUI)

To utilize the Graphical User Interface (GUI), follow these steps:

1. **Launch the GUI:**
   - Open the `gui.ipynb` file in Jupyter Notebook or JupyterLab.
   - Execute the notebook cells to launch the GUI interface.
   - Upload your receipt image and see the results
