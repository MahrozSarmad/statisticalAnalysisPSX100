import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats
import numpy as np
import seaborn as sns
def load_data():
    data = pd.read_csv('stock-exchange-kse-100pakistan.csv')
    return data

def show_info(data):
    buf = []
    buf.append("Column Names:\n" + str(data.columns.tolist()))
    buf.append("\nMissing Values:\n" + str(data.isnull().sum()))
    buf.append("\nData Types:\n" + str(data.dtypes))
    return "\n\n".join(buf)

def clean_data(data):
    data = data.copy()
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    for col in ['Open', 'High', 'Low', 'Close', 'Change', 'Volume']:
        data[col] = pd.to_numeric(data[col].astype(str).str.replace(',', ''), errors='coerce')
    return data

def plot_close_hist(data):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(data['Close'].dropna(), bins=50, color='skyblue', edgecolor='black')
    ax.set_title('Distribution of Closing Prices')
    ax.set_xlabel('Closing Price')
    ax.set_ylabel('Frequency')
    return fig

def plot_volume_pie(data):
    data['Year'] = data['Date'].dt.year
    volume_by_year = data.groupby('Year')['Volume'].sum().dropna()
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(volume_by_year, labels=volume_by_year.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Total Volume Traded by Year')
    return fig

def plot_box_close(data):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.boxplot(data['Close'].dropna(), vert=False)
    ax.set_title('Box Plot of Closing Prices')
    ax.set_xlabel('Closing Price')
    return fig

def plot_regression_close_volume(data):
    data = data.dropna(subset=['Volume', 'Close'])
    X = data[['Volume']]
    y = data['Close']
    model = LinearRegression()
    model.fit(X, y)
    data['Predicted_Close'] = model.predict(X)
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.scatter(data['Volume'], data['Close'], color='gray', label='Actual')
    ax.plot(data['Volume'], data['Predicted_Close'], color='red', label='Regression Line')
    ax.set_title('Regression: Close vs Volume')
    ax.set_xlabel('Volume')
    ax.set_ylabel('Close')
    ax.legend()
    return fig, model.coef_[0], model.intercept_



def plot_line_ohlc(data):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(data['Date'], data['Open'], label='Open', linewidth=1)
    ax.plot(data['Date'], data['High'], label='High', linewidth=1)
    ax.plot(data['Date'], data['Low'], label='Low', linewidth=1)
    ax.plot(data['Date'], data['Close'], label='Close', linewidth=1)
    ax.set_title('Line Chart - Open, High, Low, Close Prices Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True)
    fig.autofmt_xdate()
    plt.tight_layout()
    return fig

def plot_close_with_normal_curve(data):
    close = data['Close'].dropna()
    mu, sigma = stats.norm.fit(close)
    
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.histplot(close, bins=30, kde=False, stat='density', color='lightgreen', edgecolor='black', ax=ax)
    
    x = np.linspace(close.min(), close.max(), 100)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r', label='Normal PDF')
    
    ax.set_title('Closing Price Distribution with Normal Curve')
    ax.set_xlabel('Closing Price')
    ax.set_ylabel('Density')
    ax.legend()
    plt.tight_layout()
    
    return fig, mu, sigma

def calculate_close_statistics(data):
    """
    Calculate basic statistical measures for closing prices
    
    Args:
        data (pd.DataFrame): DataFrame containing stock data with 'Close' column
    
    Returns:
        dict: Dictionary containing mean, median, variance, and standard deviation
    """
    close = data['Close']
    
    # Calculate statistics
    stats = {
        'mean': round(close.mean(), 2),
        'median': round(close.median(), 2),
        'variance': round(close.var(), 2),
        'std_dev': round(close.std(), 2)
    }
    
    return stats

def calculate_confidence_interval(data, confidence=0.95):
    """
    Calculate confidence interval for closing prices
    
    Args:
        data (pd.DataFrame): DataFrame containing stock data
        confidence (float): Confidence level (default: 0.95)
    
    Returns:
        tuple: Sample size, mean, std_dev, lower_bound, upper_bound
    """
    import scipy.stats as stats
    import numpy as np
    
    close_prices = data['Close']
    n = len(close_prices)
    mean = close_prices.mean()
    std_dev = close_prices.std()
    
    t_critical = stats.t.ppf((1 + confidence) / 2, df=n-1)
    margin_of_error = t_critical * (std_dev / np.sqrt(n))
    
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    
    return n, mean, std_dev, lower_bound, upper_bound

def plot_bar_chart(data):
    """
    Create a bar chart showing average closing prices by year
    
    Args:
        data (pd.DataFrame): DataFrame containing stock data
    
    Returns:
        matplotlib.figure.Figure: The bar chart figure
    """
    # Calculate yearly averages
    data['Year'] = pd.to_datetime(data['Date']).dt.year
    yearly_avg = data.groupby('Year')['Close'].mean()
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create bars
    bars = ax.bar(yearly_avg.index, yearly_avg.values, color='red', edgecolor='black')
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:,.0f}',
                ha='center', va='bottom')
    
    # Customize plot
    ax.set_title('Average Closing Price by Year', pad=15)
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Closing Price')
    plt.xticks(rotation=45)
    
    # Add grid
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    return fig
