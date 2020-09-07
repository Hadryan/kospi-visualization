{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas-datareader in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (0.8.1)\n",
      "Requirement already satisfied: pandas>=0.21 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from pandas-datareader) (1.0.1)\n",
      "Requirement already satisfied: requests>=2.3.0 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from pandas-datareader) (2.22.0)\n",
      "Requirement already satisfied: lxml in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from pandas-datareader) (4.5.0)\n",
      "Requirement already satisfied: python-dateutil>=2.6.1 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from pandas>=0.21->pandas-datareader) (2.8.1)\n",
      "Requirement already satisfied: pytz>=2017.2 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from pandas>=0.21->pandas-datareader) (2019.3)\n",
      "Requirement already satisfied: numpy>=1.13.3 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from pandas>=0.21->pandas-datareader) (1.18.1)\n",
      "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from requests>=2.3.0->pandas-datareader) (1.25.8)\n",
      "Requirement already satisfied: idna<2.9,>=2.5 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from requests>=2.3.0->pandas-datareader) (2.8)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from requests>=2.3.0->pandas-datareader) (2019.11.28)\n",
      "Requirement already satisfied: chardet<3.1.0,>=3.0.2 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from requests>=2.3.0->pandas-datareader) (3.0.4)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from python-dateutil>=2.6.1->pandas>=0.21->pandas-datareader) (1.14.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas-datareader"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\sky_a\\anaconda3\\lib\\site-packages\\pandas_datareader\\compat\\__init__.py:7: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.\n",
      "  from pandas.util.testing import assert_frame_equal\n"
     ]
    }
   ],
   "source": [
    "import pandas_datareader as pdr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 239,
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "\n",
    "start = datetime(2020,6,1)\n",
    "end= datetime(2020,6,30)\n",
    "\n",
    "df = pdr.get_data_yahoo('^KS11',start,end)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 240,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2020-06-01</th>\n",
       "      <td>2065.379883</td>\n",
       "      <td>2035.630005</td>\n",
       "      <td>2037.040039</td>\n",
       "      <td>2065.080078</td>\n",
       "      <td>997300</td>\n",
       "      <td>2065.080078</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-02</th>\n",
       "      <td>2089.429932</td>\n",
       "      <td>2059.139893</td>\n",
       "      <td>2061.449951</td>\n",
       "      <td>2087.189941</td>\n",
       "      <td>1000300</td>\n",
       "      <td>2087.189941</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-03</th>\n",
       "      <td>2156.550049</td>\n",
       "      <td>2107.689941</td>\n",
       "      <td>2108.550049</td>\n",
       "      <td>2147.000000</td>\n",
       "      <td>1152000</td>\n",
       "      <td>2147.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-04</th>\n",
       "      <td>2191.000000</td>\n",
       "      <td>2139.679932</td>\n",
       "      <td>2181.639893</td>\n",
       "      <td>2151.179932</td>\n",
       "      <td>1393300</td>\n",
       "      <td>2151.179932</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-05</th>\n",
       "      <td>2187.250000</td>\n",
       "      <td>2138.179932</td>\n",
       "      <td>2151.169922</td>\n",
       "      <td>2181.870117</td>\n",
       "      <td>854600</td>\n",
       "      <td>2181.870117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-08</th>\n",
       "      <td>2217.209961</td>\n",
       "      <td>2174.959961</td>\n",
       "      <td>2215.600098</td>\n",
       "      <td>2184.290039</td>\n",
       "      <td>854000</td>\n",
       "      <td>2184.290039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-09</th>\n",
       "      <td>2212.169922</td>\n",
       "      <td>2166.010010</td>\n",
       "      <td>2206.229980</td>\n",
       "      <td>2188.919922</td>\n",
       "      <td>817100</td>\n",
       "      <td>2188.919922</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-10</th>\n",
       "      <td>2200.679932</td>\n",
       "      <td>2178.120117</td>\n",
       "      <td>2187.909912</td>\n",
       "      <td>2195.689941</td>\n",
       "      <td>706300</td>\n",
       "      <td>2195.689941</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-11</th>\n",
       "      <td>2200.719971</td>\n",
       "      <td>2148.510010</td>\n",
       "      <td>2184.360107</td>\n",
       "      <td>2176.780029</td>\n",
       "      <td>827400</td>\n",
       "      <td>2176.780029</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-12</th>\n",
       "      <td>2137.120117</td>\n",
       "      <td>2084.629883</td>\n",
       "      <td>2088.239990</td>\n",
       "      <td>2132.300049</td>\n",
       "      <td>689900</td>\n",
       "      <td>2132.300049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-15</th>\n",
       "      <td>2129.669922</td>\n",
       "      <td>2030.819946</td>\n",
       "      <td>2114.409912</td>\n",
       "      <td>2030.819946</td>\n",
       "      <td>1071600</td>\n",
       "      <td>2030.819946</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-16</th>\n",
       "      <td>2138.080078</td>\n",
       "      <td>2079.020020</td>\n",
       "      <td>2091.090088</td>\n",
       "      <td>2138.050049</td>\n",
       "      <td>973300</td>\n",
       "      <td>2138.050049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-17</th>\n",
       "      <td>2154.370117</td>\n",
       "      <td>2105.260010</td>\n",
       "      <td>2133.179932</td>\n",
       "      <td>2141.050049</td>\n",
       "      <td>927200</td>\n",
       "      <td>2141.050049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-18</th>\n",
       "      <td>2145.129883</td>\n",
       "      <td>2120.290039</td>\n",
       "      <td>2134.350098</td>\n",
       "      <td>2133.479980</td>\n",
       "      <td>767100</td>\n",
       "      <td>2133.479980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-19</th>\n",
       "      <td>2153.570068</td>\n",
       "      <td>2108.909912</td>\n",
       "      <td>2153.090088</td>\n",
       "      <td>2141.320068</td>\n",
       "      <td>1079300</td>\n",
       "      <td>2141.320068</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-22</th>\n",
       "      <td>2142.879883</td>\n",
       "      <td>2122.100098</td>\n",
       "      <td>2126.379883</td>\n",
       "      <td>2126.729980</td>\n",
       "      <td>789400</td>\n",
       "      <td>2126.729980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-23</th>\n",
       "      <td>2158.149902</td>\n",
       "      <td>2110.510010</td>\n",
       "      <td>2149.129883</td>\n",
       "      <td>2131.239990</td>\n",
       "      <td>917600</td>\n",
       "      <td>2131.239990</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-24</th>\n",
       "      <td>2171.860107</td>\n",
       "      <td>2143.909912</td>\n",
       "      <td>2145.929932</td>\n",
       "      <td>2161.510010</td>\n",
       "      <td>913900</td>\n",
       "      <td>2161.510010</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-25</th>\n",
       "      <td>2143.330078</td>\n",
       "      <td>2112.370117</td>\n",
       "      <td>2130.449951</td>\n",
       "      <td>2112.370117</td>\n",
       "      <td>1017700</td>\n",
       "      <td>2112.370117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-26</th>\n",
       "      <td>2142.040039</td>\n",
       "      <td>2115.250000</td>\n",
       "      <td>2137.469971</td>\n",
       "      <td>2134.649902</td>\n",
       "      <td>761000</td>\n",
       "      <td>2134.649902</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-29</th>\n",
       "      <td>2120.500000</td>\n",
       "      <td>2087.840088</td>\n",
       "      <td>2105.540039</td>\n",
       "      <td>2093.479980</td>\n",
       "      <td>643200</td>\n",
       "      <td>2093.479980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-30</th>\n",
       "      <td>2134.379883</td>\n",
       "      <td>2108.260010</td>\n",
       "      <td>2124.379883</td>\n",
       "      <td>2108.330078</td>\n",
       "      <td>700043</td>\n",
       "      <td>2108.330078</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   High          Low         Open        Close   Volume  \\\n",
       "Date                                                                      \n",
       "2020-06-01  2065.379883  2035.630005  2037.040039  2065.080078   997300   \n",
       "2020-06-02  2089.429932  2059.139893  2061.449951  2087.189941  1000300   \n",
       "2020-06-03  2156.550049  2107.689941  2108.550049  2147.000000  1152000   \n",
       "2020-06-04  2191.000000  2139.679932  2181.639893  2151.179932  1393300   \n",
       "2020-06-05  2187.250000  2138.179932  2151.169922  2181.870117   854600   \n",
       "2020-06-08  2217.209961  2174.959961  2215.600098  2184.290039   854000   \n",
       "2020-06-09  2212.169922  2166.010010  2206.229980  2188.919922   817100   \n",
       "2020-06-10  2200.679932  2178.120117  2187.909912  2195.689941   706300   \n",
       "2020-06-11  2200.719971  2148.510010  2184.360107  2176.780029   827400   \n",
       "2020-06-12  2137.120117  2084.629883  2088.239990  2132.300049   689900   \n",
       "2020-06-15  2129.669922  2030.819946  2114.409912  2030.819946  1071600   \n",
       "2020-06-16  2138.080078  2079.020020  2091.090088  2138.050049   973300   \n",
       "2020-06-17  2154.370117  2105.260010  2133.179932  2141.050049   927200   \n",
       "2020-06-18  2145.129883  2120.290039  2134.350098  2133.479980   767100   \n",
       "2020-06-19  2153.570068  2108.909912  2153.090088  2141.320068  1079300   \n",
       "2020-06-22  2142.879883  2122.100098  2126.379883  2126.729980   789400   \n",
       "2020-06-23  2158.149902  2110.510010  2149.129883  2131.239990   917600   \n",
       "2020-06-24  2171.860107  2143.909912  2145.929932  2161.510010   913900   \n",
       "2020-06-25  2143.330078  2112.370117  2130.449951  2112.370117  1017700   \n",
       "2020-06-26  2142.040039  2115.250000  2137.469971  2134.649902   761000   \n",
       "2020-06-29  2120.500000  2087.840088  2105.540039  2093.479980   643200   \n",
       "2020-06-30  2134.379883  2108.260010  2124.379883  2108.330078   700043   \n",
       "\n",
       "              Adj Close  \n",
       "Date                     \n",
       "2020-06-01  2065.080078  \n",
       "2020-06-02  2087.189941  \n",
       "2020-06-03  2147.000000  \n",
       "2020-06-04  2151.179932  \n",
       "2020-06-05  2181.870117  \n",
       "2020-06-08  2184.290039  \n",
       "2020-06-09  2188.919922  \n",
       "2020-06-10  2195.689941  \n",
       "2020-06-11  2176.780029  \n",
       "2020-06-12  2132.300049  \n",
       "2020-06-15  2030.819946  \n",
       "2020-06-16  2138.050049  \n",
       "2020-06-17  2141.050049  \n",
       "2020-06-18  2133.479980  \n",
       "2020-06-19  2141.320068  \n",
       "2020-06-22  2126.729980  \n",
       "2020-06-23  2131.239990  \n",
       "2020-06-24  2161.510010  \n",
       "2020-06-25  2112.370117  \n",
       "2020-06-26  2134.649902  \n",
       "2020-06-29  2093.479980  \n",
       "2020-06-30  2108.330078  "
      ]
     },
     "execution_count": 240,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2020-06-01</th>\n",
       "      <td>2065.080078</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-02</th>\n",
       "      <td>2087.189941</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-03</th>\n",
       "      <td>2147.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-04</th>\n",
       "      <td>2151.179932</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-05</th>\n",
       "      <td>2181.870117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-08</th>\n",
       "      <td>2184.290039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-09</th>\n",
       "      <td>2188.919922</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-10</th>\n",
       "      <td>2195.689941</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-11</th>\n",
       "      <td>2176.780029</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-12</th>\n",
       "      <td>2132.300049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-15</th>\n",
       "      <td>2030.819946</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-16</th>\n",
       "      <td>2138.050049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-17</th>\n",
       "      <td>2141.050049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-18</th>\n",
       "      <td>2133.479980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-19</th>\n",
       "      <td>2141.320068</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-22</th>\n",
       "      <td>2126.729980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-23</th>\n",
       "      <td>2131.239990</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-24</th>\n",
       "      <td>2161.510010</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-25</th>\n",
       "      <td>2112.370117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-26</th>\n",
       "      <td>2134.649902</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-29</th>\n",
       "      <td>2093.479980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-30</th>\n",
       "      <td>2108.330078</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Close\n",
       "Date                   \n",
       "2020-06-01  2065.080078\n",
       "2020-06-02  2087.189941\n",
       "2020-06-03  2147.000000\n",
       "2020-06-04  2151.179932\n",
       "2020-06-05  2181.870117\n",
       "2020-06-08  2184.290039\n",
       "2020-06-09  2188.919922\n",
       "2020-06-10  2195.689941\n",
       "2020-06-11  2176.780029\n",
       "2020-06-12  2132.300049\n",
       "2020-06-15  2030.819946\n",
       "2020-06-16  2138.050049\n",
       "2020-06-17  2141.050049\n",
       "2020-06-18  2133.479980\n",
       "2020-06-19  2141.320068\n",
       "2020-06-22  2126.729980\n",
       "2020-06-23  2131.239990\n",
       "2020-06-24  2161.510010\n",
       "2020-06-25  2112.370117\n",
       "2020-06-26  2134.649902\n",
       "2020-06-29  2093.479980\n",
       "2020-06-30  2108.330078"
      ]
     },
     "execution_count": 241,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Kospi=df.iloc[:,3:4]\n",
    "Kospi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Close</th>\n",
       "      <th>model</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6.01</th>\n",
       "      <td>2065.080078</td>\n",
       "      <td>11/12 2/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.02</th>\n",
       "      <td>2087.189941</td>\n",
       "      <td>11/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.03</th>\n",
       "      <td>2147.000000</td>\n",
       "      <td>10/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.04</th>\n",
       "      <td>2151.179932</td>\n",
       "      <td>10/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.05</th>\n",
       "      <td>2181.870117</td>\n",
       "      <td>10/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.08</th>\n",
       "      <td>2184.290039</td>\n",
       "      <td>10/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.09</th>\n",
       "      <td>2188.919922</td>\n",
       "      <td>9/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.10</th>\n",
       "      <td>2195.689941</td>\n",
       "      <td>8/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.11</th>\n",
       "      <td>2176.780029</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.12</th>\n",
       "      <td>2132.300049</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.15</th>\n",
       "      <td>2030.819946</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.16</th>\n",
       "      <td>2138.050049</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.17</th>\n",
       "      <td>2141.050049</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.18</th>\n",
       "      <td>2133.479980</td>\n",
       "      <td>7/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.19</th>\n",
       "      <td>2141.320068</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.22</th>\n",
       "      <td>2126.729980</td>\n",
       "      <td>5/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.23</th>\n",
       "      <td>2131.239990</td>\n",
       "      <td>3/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.24</th>\n",
       "      <td>2161.510010</td>\n",
       "      <td>3/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.25</th>\n",
       "      <td>2112.370117</td>\n",
       "      <td>3/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.26</th>\n",
       "      <td>2134.649902</td>\n",
       "      <td>2/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.29</th>\n",
       "      <td>2093.479980</td>\n",
       "      <td>2/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.30</th>\n",
       "      <td>2108.330078</td>\n",
       "      <td>2/12 0/6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Close      model\n",
       "6.01  2065.080078  11/12 2/6\n",
       "6.02  2087.189941  11/12 0/6\n",
       "6.03  2147.000000  10/12 0/6\n",
       "6.04  2151.179932  10/12 0/6\n",
       "6.05  2181.870117  10/12 0/6\n",
       "6.08  2184.290039  10/12 0/6\n",
       "6.09  2188.919922   9/12 0/6\n",
       "6.10  2195.689941   8/12 0/6\n",
       "6.11  2176.780029   6/12 0/6\n",
       "6.12  2132.300049   6/12 0/6\n",
       "6.15  2030.819946   6/12 0/6\n",
       "6.16  2138.050049   6/12 0/6\n",
       "6.17  2141.050049   6/12 0/6\n",
       "6.18  2133.479980   7/12 0/6\n",
       "6.19  2141.320068   6/12 0/6\n",
       "6.22  2126.729980   5/12 0/6\n",
       "6.23  2131.239990   3/12 0/6\n",
       "6.24  2161.510010   3/12 0/6\n",
       "6.25  2112.370117   3/12 0/6\n",
       "6.26  2134.649902   2/12 0/6\n",
       "6.29  2093.479980   2/12 0/6\n",
       "6.30  2108.330078   2/12 0/6"
      ]
     },
     "execution_count": 242,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "Kospi.index=np.array([6.01,6.02,6.03,6.04,6.05,6.08,6.09,6.10,6.11,6.12,6.15,6.16,6.17,6.18,6.19,6.22,6.23,6.24,6.25,6.26,6.29,6.30],dtype=np.float64)\n",
    "Kospi['model']=['11/12 2/6' , '11/12 0/6' ,'10/12 0/6' , '10/12 0/6' ,'10/12 0/6' ,'10/12 0/6' , '9/12 0/6' , \n",
    "             '8/12 0/6','6/12 0/6' , '6/12 0/6','6/12 0/6','6/12 0/6','6/12 0/6','7/12 0/6','6/12 0/6','5/12 0/6',\n",
    "            '3/12 0/6' ,'3/12 0/6','3/12 0/6','2/12 0/6','2/12 0/6' , '2/12 0/6']\n",
    "Kospi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Close</th>\n",
       "      <th>model</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6.01</th>\n",
       "      <td>2065.080078</td>\n",
       "      <td>11/12 2/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.02</th>\n",
       "      <td>2087.189941</td>\n",
       "      <td>11/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.03</th>\n",
       "      <td>2147.000000</td>\n",
       "      <td>10/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.04</th>\n",
       "      <td>2151.179932</td>\n",
       "      <td>10/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.05</th>\n",
       "      <td>2181.870117</td>\n",
       "      <td>10/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.08</th>\n",
       "      <td>2184.290039</td>\n",
       "      <td>10/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.09</th>\n",
       "      <td>2188.919922</td>\n",
       "      <td>9/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.10</th>\n",
       "      <td>2195.689941</td>\n",
       "      <td>8/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.11</th>\n",
       "      <td>2176.780029</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.12</th>\n",
       "      <td>2132.300049</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.15</th>\n",
       "      <td>2030.819946</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.16</th>\n",
       "      <td>2138.050049</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.17</th>\n",
       "      <td>2141.050049</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.18</th>\n",
       "      <td>2133.479980</td>\n",
       "      <td>7/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.19</th>\n",
       "      <td>2141.320068</td>\n",
       "      <td>6/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.22</th>\n",
       "      <td>2126.729980</td>\n",
       "      <td>5/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.23</th>\n",
       "      <td>2131.239990</td>\n",
       "      <td>3/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.24</th>\n",
       "      <td>2161.510010</td>\n",
       "      <td>3/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.25</th>\n",
       "      <td>2112.370117</td>\n",
       "      <td>3/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.26</th>\n",
       "      <td>2134.649902</td>\n",
       "      <td>2/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.29</th>\n",
       "      <td>2093.479980</td>\n",
       "      <td>2/12 0/6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6.30</th>\n",
       "      <td>2108.330078</td>\n",
       "      <td>2/12 0/6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Close      model\n",
       "6.01  2065.080078  11/12 2/6\n",
       "6.02  2087.189941  11/12 0/6\n",
       "6.03  2147.000000  10/12 0/6\n",
       "6.04  2151.179932  10/12 0/6\n",
       "6.05  2181.870117  10/12 0/6\n",
       "6.08  2184.290039  10/12 0/6\n",
       "6.09  2188.919922   9/12 0/6\n",
       "6.10  2195.689941   8/12 0/6\n",
       "6.11  2176.780029   6/12 0/6\n",
       "6.12  2132.300049   6/12 0/6\n",
       "6.15  2030.819946   6/12 0/6\n",
       "6.16  2138.050049   6/12 0/6\n",
       "6.17  2141.050049   6/12 0/6\n",
       "6.18  2133.479980   7/12 0/6\n",
       "6.19  2141.320068   6/12 0/6\n",
       "6.22  2126.729980   5/12 0/6\n",
       "6.23  2131.239990   3/12 0/6\n",
       "6.24  2161.510010   3/12 0/6\n",
       "6.25  2112.370117   3/12 0/6\n",
       "6.26  2134.649902   2/12 0/6\n",
       "6.29  2093.479980   2/12 0/6\n",
       "6.30  2108.330078   2/12 0/6"
      ]
     },
     "execution_count": 243,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "Kospi=pd.DataFrame(Kospi)\n",
    "Kospi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting plotly\n",
      "  Using cached plotly-4.8.2-py2.py3-none-any.whl (11.5 MB)\n",
      "Requirement already satisfied: six in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from plotly) (1.14.0)\n",
      "Requirement already satisfied: retrying>=1.3.3 in c:\\users\\sky_a\\anaconda3\\lib\\site-packages (from plotly) (1.3.3)\n",
      "Installing collected packages: plotly\n",
      "Successfully installed plotly-4.8.2\n"
     ]
    }
   ],
   "source": [
    "!pip install plotly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-latest.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "line": {
          "color": "Black"
         },
         "name": "Close",
         "type": "scatter",
         "x": [
          6.01,
          6.02,
          6.03,
          6.04,
          6.05,
          6.08,
          6.09,
          6.1,
          6.11,
          6.12,
          6.15,
          6.16,
          6.17,
          6.18,
          6.19,
          6.22,
          6.23,
          6.24,
          6.25,
          6.26,
          6.29,
          6.3
         ],
         "y": [
          2065.080078125,
          2087.18994140625,
          2147,
          2151.179931640625,
          2181.8701171875,
          2184.2900390625,
          2188.919921875,
          2195.68994140625,
          2176.780029296875,
          2132.300048828125,
          2030.8199462890625,
          2138.050048828125,
          2141.050048828125,
          2133.47998046875,
          2141.320068359375,
          2126.72998046875,
          2131.239990234375,
          2161.510009765625,
          2112.3701171875,
          2134.64990234375,
          2093.47998046875,
          2108.330078125
         ]
        },
        {
         "name": "11/12 2/6",
         "type": "scatter",
         "x": [
          6.01,
          6.02
         ],
         "y": [
          2065.080078125,
          2087.18994140625
         ]
        },
        {
         "name": "10/12 0/6",
         "type": "scatter",
         "x": [
          6.03,
          6.04,
          6.05,
          6.08
         ],
         "y": [
          2147,
          2151.179931640625,
          2181.8701171875,
          2184.2900390625
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "9/12 0/6",
         "type": "scatter",
         "x": [
          6.09
         ],
         "y": [
          2188.919921875
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "8/12 0/6",
         "type": "scatter",
         "x": [
          6.1
         ],
         "y": [
          2195.68994140625
         ]
        },
        {
         "name": "6/12 0/6",
         "type": "scatter",
         "x": [
          6.11,
          6.12,
          6.15,
          6.16,
          6.17
         ],
         "y": [
          2176.780029296875,
          2132.300048828125,
          2030.8199462890625,
          2138.050048828125,
          2141.050048828125
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "7/12 0/6",
         "type": "scatter",
         "x": [
          6.18
         ],
         "y": [
          2133.47998046875
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "6/12 0/6",
         "type": "scatter",
         "x": [
          6.19
         ],
         "y": [
          2141.320068359375
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "5/12 0/6",
         "type": "scatter",
         "x": [
          6.22
         ],
         "y": [
          2126.72998046875
         ]
        },
        {
         "name": "3/12 0/6",
         "type": "scatter",
         "x": [
          6.23,
          6.24,
          6.25
         ],
         "y": [
          2131.239990234375,
          2161.510009765625,
          2112.3701171875
         ]
        },
        {
         "name": "2/12 0/6",
         "type": "scatter",
         "x": [
          6.26,
          6.29,
          6.3
         ],
         "y": [
          2134.64990234375,
          2093.47998046875,
          2108.330078125
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #1",
         "text": [
          "30"
         ],
         "type": "scatter",
         "x": [
          6.03
         ],
         "y": [
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #2",
         "text": [
          "15"
         ],
         "type": "scatter",
         "x": [
          6.07
         ],
         "y": [
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #3",
         "text": [
          "10",
          "10"
         ],
         "type": "scatter",
         "x": [
          6.11,
          6.21
         ],
         "y": [
          2220,
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #4",
         "text": [
          "0",
          "0"
         ],
         "type": "scatter",
         "x": [
          6.15,
          6.28
         ],
         "y": [
          2220,
          2220,
          2220
         ]
        },
        {
         "line": {
          "color": "Black"
         },
         "name": "Close",
         "type": "scatter",
         "x": [
          6.01,
          6.02,
          6.03,
          6.04,
          6.05,
          6.08,
          6.09,
          6.1,
          6.11,
          6.12,
          6.15,
          6.16,
          6.17,
          6.18,
          6.19,
          6.22,
          6.23,
          6.24,
          6.25,
          6.26,
          6.29,
          6.3
         ],
         "y": [
          2065.080078125,
          2087.18994140625,
          2147,
          2151.179931640625,
          2181.8701171875,
          2184.2900390625,
          2188.919921875,
          2195.68994140625,
          2176.780029296875,
          2132.300048828125,
          2030.8199462890625,
          2138.050048828125,
          2141.050048828125,
          2133.47998046875,
          2141.320068359375,
          2126.72998046875,
          2131.239990234375,
          2161.510009765625,
          2112.3701171875,
          2134.64990234375,
          2093.47998046875,
          2108.330078125
         ]
        },
        {
         "name": "11/12 2/6",
         "type": "scatter",
         "x": [
          6.01,
          6.02
         ],
         "y": [
          2065.080078125,
          2087.18994140625
         ]
        },
        {
         "name": "10/12 0/6",
         "type": "scatter",
         "x": [
          6.03,
          6.04,
          6.05,
          6.08
         ],
         "y": [
          2147,
          2151.179931640625,
          2181.8701171875,
          2184.2900390625
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "9/12 0/6",
         "type": "scatter",
         "x": [
          6.09
         ],
         "y": [
          2188.919921875
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "8/12 0/6",
         "type": "scatter",
         "x": [
          6.1
         ],
         "y": [
          2195.68994140625
         ]
        },
        {
         "name": "6/12 0/6",
         "type": "scatter",
         "x": [
          6.11,
          6.12,
          6.15,
          6.16,
          6.17
         ],
         "y": [
          2176.780029296875,
          2132.300048828125,
          2030.8199462890625,
          2138.050048828125,
          2141.050048828125
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "7/12 0/6",
         "type": "scatter",
         "x": [
          6.18
         ],
         "y": [
          2133.47998046875
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "6/12 0/6",
         "type": "scatter",
         "x": [
          6.19
         ],
         "y": [
          2141.320068359375
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "5/12 0/6",
         "type": "scatter",
         "x": [
          6.22
         ],
         "y": [
          2126.72998046875
         ]
        },
        {
         "name": "3/12 0/6",
         "type": "scatter",
         "x": [
          6.23,
          6.24,
          6.25
         ],
         "y": [
          2131.239990234375,
          2161.510009765625,
          2112.3701171875
         ]
        },
        {
         "name": "2/12 0/6",
         "type": "scatter",
         "x": [
          6.26,
          6.29,
          6.3
         ],
         "y": [
          2134.64990234375,
          2093.47998046875,
          2108.330078125
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #1",
         "text": [
          "30"
         ],
         "type": "scatter",
         "x": [
          6.03
         ],
         "y": [
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #2",
         "text": [
          "15"
         ],
         "type": "scatter",
         "x": [
          6.07
         ],
         "y": [
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #3",
         "text": [
          "10",
          "10"
         ],
         "type": "scatter",
         "x": [
          6.11,
          6.21
         ],
         "y": [
          2220,
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #4",
         "text": [
          "0",
          "0"
         ],
         "type": "scatter",
         "x": [
          6.15,
          6.28
         ],
         "y": [
          2220,
          2220,
          2220
         ]
        },
        {
         "line": {
          "color": "Black"
         },
         "name": "Close",
         "type": "scatter",
         "x": [
          6.01,
          6.02,
          6.03,
          6.04,
          6.05,
          6.08,
          6.09,
          6.1,
          6.11,
          6.12,
          6.15,
          6.16,
          6.17,
          6.18,
          6.19,
          6.22,
          6.23,
          6.24,
          6.25,
          6.26,
          6.29,
          6.3
         ],
         "y": [
          2065.080078125,
          2087.18994140625,
          2147,
          2151.179931640625,
          2181.8701171875,
          2184.2900390625,
          2188.919921875,
          2195.68994140625,
          2176.780029296875,
          2132.300048828125,
          2030.8199462890625,
          2138.050048828125,
          2141.050048828125,
          2133.47998046875,
          2141.320068359375,
          2126.72998046875,
          2131.239990234375,
          2161.510009765625,
          2112.3701171875,
          2134.64990234375,
          2093.47998046875,
          2108.330078125
         ]
        },
        {
         "name": "11/12 2/6",
         "type": "scatter",
         "x": [
          6.01,
          6.02
         ],
         "y": [
          2065.080078125,
          2087.18994140625
         ]
        },
        {
         "name": "10/12 0/6",
         "type": "scatter",
         "x": [
          6.03,
          6.04,
          6.05,
          6.08
         ],
         "y": [
          2147,
          2151.179931640625,
          2181.8701171875,
          2184.2900390625
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "9/12 0/6",
         "type": "scatter",
         "x": [
          6.09
         ],
         "y": [
          2188.919921875
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "8/12 0/6",
         "type": "scatter",
         "x": [
          6.1
         ],
         "y": [
          2195.68994140625
         ]
        },
        {
         "name": "6/12 0/6",
         "type": "scatter",
         "x": [
          6.11,
          6.12,
          6.15,
          6.16,
          6.17
         ],
         "y": [
          2176.780029296875,
          2132.300048828125,
          2030.8199462890625,
          2138.050048828125,
          2141.050048828125
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "7/12 0/6",
         "type": "scatter",
         "x": [
          6.18
         ],
         "y": [
          2133.47998046875
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "6/12 0/6",
         "type": "scatter",
         "x": [
          6.19
         ],
         "y": [
          2141.320068359375
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "5/12 0/6",
         "type": "scatter",
         "x": [
          6.22
         ],
         "y": [
          2126.72998046875
         ]
        },
        {
         "name": "3/12 0/6",
         "type": "scatter",
         "x": [
          6.23,
          6.24,
          6.25
         ],
         "y": [
          2131.239990234375,
          2161.510009765625,
          2112.3701171875
         ]
        },
        {
         "name": "2/12 0/6",
         "type": "scatter",
         "x": [
          6.26,
          6.29,
          6.3
         ],
         "y": [
          2134.64990234375,
          2093.47998046875,
          2108.330078125
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #1",
         "text": [
          "30"
         ],
         "type": "scatter",
         "x": [
          6.03
         ],
         "y": [
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #2",
         "text": [
          "15"
         ],
         "type": "scatter",
         "x": [
          6.07
         ],
         "y": [
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #3",
         "text": [
          "10",
          "10"
         ],
         "type": "scatter",
         "x": [
          6.11,
          6.21
         ],
         "y": [
          2220,
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #4",
         "text": [
          "0",
          "0"
         ],
         "type": "scatter",
         "x": [
          6.15,
          6.28
         ],
         "y": [
          2220,
          2220,
          2220
         ]
        },
        {
         "line": {
          "color": "Black"
         },
         "name": "Close",
         "type": "scatter",
         "x": [
          6.01,
          6.02,
          6.03,
          6.04,
          6.05,
          6.08,
          6.09,
          6.1,
          6.11,
          6.12,
          6.15,
          6.16,
          6.17,
          6.18,
          6.19,
          6.22,
          6.23,
          6.24,
          6.25,
          6.26,
          6.29,
          6.3
         ],
         "y": [
          2065.080078125,
          2087.18994140625,
          2147,
          2151.179931640625,
          2181.8701171875,
          2184.2900390625,
          2188.919921875,
          2195.68994140625,
          2176.780029296875,
          2132.300048828125,
          2030.8199462890625,
          2138.050048828125,
          2141.050048828125,
          2133.47998046875,
          2141.320068359375,
          2126.72998046875,
          2131.239990234375,
          2161.510009765625,
          2112.3701171875,
          2134.64990234375,
          2093.47998046875,
          2108.330078125
         ]
        },
        {
         "name": "11/12 2/6",
         "type": "scatter",
         "x": [
          6.01,
          6.02
         ],
         "y": [
          2065.080078125,
          2087.18994140625
         ]
        },
        {
         "name": "10/12 0/6",
         "type": "scatter",
         "x": [
          6.03,
          6.04,
          6.05,
          6.08
         ],
         "y": [
          2147,
          2151.179931640625,
          2181.8701171875,
          2184.2900390625
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "9/12 0/6",
         "type": "scatter",
         "x": [
          6.09
         ],
         "y": [
          2188.919921875
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "8/12 0/6",
         "type": "scatter",
         "x": [
          6.1
         ],
         "y": [
          2195.68994140625
         ]
        },
        {
         "name": "6/12 0/6",
         "type": "scatter",
         "x": [
          6.11,
          6.12,
          6.15,
          6.16,
          6.17
         ],
         "y": [
          2176.780029296875,
          2132.300048828125,
          2030.8199462890625,
          2138.050048828125,
          2141.050048828125
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "7/12 0/6",
         "type": "scatter",
         "x": [
          6.18
         ],
         "y": [
          2133.47998046875
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "6/12 0/6",
         "type": "scatter",
         "x": [
          6.19
         ],
         "y": [
          2141.320068359375
         ]
        },
        {
         "marker": {
          "size": [
           15
          ]
         },
         "name": "5/12 0/6",
         "type": "scatter",
         "x": [
          6.22
         ],
         "y": [
          2126.72998046875
         ]
        },
        {
         "name": "3/12 0/6",
         "type": "scatter",
         "x": [
          6.23,
          6.24,
          6.25
         ],
         "y": [
          2131.239990234375,
          2161.510009765625,
          2112.3701171875
         ]
        },
        {
         "name": "2/12 0/6",
         "type": "scatter",
         "x": [
          6.26,
          6.29,
          6.3
         ],
         "y": [
          2134.64990234375,
          2093.47998046875,
          2108.330078125
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #1",
         "text": [
          "30"
         ],
         "type": "scatter",
         "x": [
          6.03
         ],
         "y": [
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #2",
         "text": [
          "15"
         ],
         "type": "scatter",
         "x": [
          6.07
         ],
         "y": [
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #3",
         "text": [
          "10",
          "10"
         ],
         "type": "scatter",
         "x": [
          6.11,
          6.21
         ],
         "y": [
          2220,
          2220
         ]
        },
        {
         "mode": "markers+text",
         "name": "Weight #4",
         "text": [
          "0",
          "0"
         ],
         "type": "scatter",
         "x": [
          6.15,
          6.28
         ],
         "y": [
          2220,
          2220,
          2220
         ]
        }
       ],
       "layout": {
        "shapes": [
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.04,
          "x1": 6.04,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.1,
          "x1": 6.1,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.12,
          "x1": 6.12,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.19,
          "x1": 6.19,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.24,
          "x1": 6.24,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.04,
          "x1": 6.04,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.1,
          "x1": 6.1,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.12,
          "x1": 6.12,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.19,
          "x1": 6.19,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.24,
          "x1": 6.24,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.04,
          "x1": 6.04,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.1,
          "x1": 6.1,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.12,
          "x1": 6.12,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.19,
          "x1": 6.19,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.24,
          "x1": 6.24,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.04,
          "x1": 6.04,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.1,
          "x1": 6.1,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.12,
          "x1": 6.12,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.19,
          "x1": 6.19,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         },
         {
          "line": {
           "color": "Black",
           "dash": "dot",
           "width": 1
          },
          "type": "line",
          "x0": 6.24,
          "x1": 6.24,
          "xref": "x",
          "y0": 0,
          "y1": 2250,
          "yref": "y"
         }
        ],
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Kospi Close"
        },
        "xaxis": {
         "dtick": 0.01,
         "tick0": 6.01,
         "tickmode": "linear",
         "title": {
          "text": "days"
         }
        },
        "yaxis": {
         "range": [
          2000,
          2250
         ],
         "title": {
          "text": "Price"
         }
        }
       }
      },
      "text/html": [
       "<div>\n",
       "        \n",
       "        \n",
       "            <div id=\"158a6a8f-ae91-428d-9078-ffe8d4f850a5\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>\n",
       "            <script type=\"text/javascript\">\n",
       "                require([\"plotly\"], function(Plotly) {\n",
       "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    \n",
       "                if (document.getElementById(\"158a6a8f-ae91-428d-9078-ffe8d4f850a5\")) {\n",
       "                    Plotly.newPlot(\n",
       "                        '158a6a8f-ae91-428d-9078-ffe8d4f850a5',\n",
       "                        [{\"line\": {\"color\": \"Black\"}, \"name\": \"Close\", \"type\": \"scatter\", \"x\": [6.01, 6.02, 6.03, 6.04, 6.05, 6.08, 6.09, 6.1, 6.11, 6.12, 6.15, 6.16, 6.17, 6.18, 6.19, 6.22, 6.23, 6.24, 6.25, 6.26, 6.29, 6.3], \"y\": [2065.080078125, 2087.18994140625, 2147.0, 2151.179931640625, 2181.8701171875, 2184.2900390625, 2188.919921875, 2195.68994140625, 2176.780029296875, 2132.300048828125, 2030.8199462890625, 2138.050048828125, 2141.050048828125, 2133.47998046875, 2141.320068359375, 2126.72998046875, 2131.239990234375, 2161.510009765625, 2112.3701171875, 2134.64990234375, 2093.47998046875, 2108.330078125]}, {\"name\": \"11/12 2/6\", \"type\": \"scatter\", \"x\": [6.01, 6.02], \"y\": [2065.080078125, 2087.18994140625]}, {\"name\": \"10/12 0/6\", \"type\": \"scatter\", \"x\": [6.03, 6.04, 6.05, 6.08], \"y\": [2147.0, 2151.179931640625, 2181.8701171875, 2184.2900390625]}, {\"marker\": {\"size\": [15]}, \"name\": \"9/12 0/6\", \"type\": \"scatter\", \"x\": [6.09], \"y\": [2188.919921875]}, {\"marker\": {\"size\": [15]}, \"name\": \"8/12 0/6\", \"type\": \"scatter\", \"x\": [6.1], \"y\": [2195.68994140625]}, {\"name\": \"6/12 0/6\", \"type\": \"scatter\", \"x\": [6.11, 6.12, 6.15, 6.16, 6.17], \"y\": [2176.780029296875, 2132.300048828125, 2030.8199462890625, 2138.050048828125, 2141.050048828125]}, {\"marker\": {\"size\": [15]}, \"name\": \"7/12 0/6\", \"type\": \"scatter\", \"x\": [6.18], \"y\": [2133.47998046875]}, {\"marker\": {\"size\": [15]}, \"name\": \"6/12 0/6\", \"type\": \"scatter\", \"x\": [6.19], \"y\": [2141.320068359375]}, {\"marker\": {\"size\": [15]}, \"name\": \"5/12 0/6\", \"type\": \"scatter\", \"x\": [6.22], \"y\": [2126.72998046875]}, {\"name\": \"3/12 0/6\", \"type\": \"scatter\", \"x\": [6.23, 6.24, 6.25], \"y\": [2131.239990234375, 2161.510009765625, 2112.3701171875]}, {\"name\": \"2/12 0/6\", \"type\": \"scatter\", \"x\": [6.26, 6.29, 6.3], \"y\": [2134.64990234375, 2093.47998046875, 2108.330078125]}, {\"mode\": \"markers+text\", \"name\": \"Weight #1\", \"text\": [\"30\"], \"type\": \"scatter\", \"x\": [6.03], \"y\": [2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #2\", \"text\": [\"15\"], \"type\": \"scatter\", \"x\": [6.07], \"y\": [2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #3\", \"text\": [\"10\", \"10\"], \"type\": \"scatter\", \"x\": [6.11, 6.21], \"y\": [2220, 2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #4\", \"text\": [\"0\", \"0\"], \"type\": \"scatter\", \"x\": [6.15, 6.28], \"y\": [2220, 2220, 2220]}, {\"line\": {\"color\": \"Black\"}, \"name\": \"Close\", \"type\": \"scatter\", \"x\": [6.01, 6.02, 6.03, 6.04, 6.05, 6.08, 6.09, 6.1, 6.11, 6.12, 6.15, 6.16, 6.17, 6.18, 6.19, 6.22, 6.23, 6.24, 6.25, 6.26, 6.29, 6.3], \"y\": [2065.080078125, 2087.18994140625, 2147.0, 2151.179931640625, 2181.8701171875, 2184.2900390625, 2188.919921875, 2195.68994140625, 2176.780029296875, 2132.300048828125, 2030.8199462890625, 2138.050048828125, 2141.050048828125, 2133.47998046875, 2141.320068359375, 2126.72998046875, 2131.239990234375, 2161.510009765625, 2112.3701171875, 2134.64990234375, 2093.47998046875, 2108.330078125]}, {\"name\": \"11/12 2/6\", \"type\": \"scatter\", \"x\": [6.01, 6.02], \"y\": [2065.080078125, 2087.18994140625]}, {\"name\": \"10/12 0/6\", \"type\": \"scatter\", \"x\": [6.03, 6.04, 6.05, 6.08], \"y\": [2147.0, 2151.179931640625, 2181.8701171875, 2184.2900390625]}, {\"marker\": {\"size\": [15]}, \"name\": \"9/12 0/6\", \"type\": \"scatter\", \"x\": [6.09], \"y\": [2188.919921875]}, {\"marker\": {\"size\": [15]}, \"name\": \"8/12 0/6\", \"type\": \"scatter\", \"x\": [6.1], \"y\": [2195.68994140625]}, {\"name\": \"6/12 0/6\", \"type\": \"scatter\", \"x\": [6.11, 6.12, 6.15, 6.16, 6.17], \"y\": [2176.780029296875, 2132.300048828125, 2030.8199462890625, 2138.050048828125, 2141.050048828125]}, {\"marker\": {\"size\": [15]}, \"name\": \"7/12 0/6\", \"type\": \"scatter\", \"x\": [6.18], \"y\": [2133.47998046875]}, {\"marker\": {\"size\": [15]}, \"name\": \"6/12 0/6\", \"type\": \"scatter\", \"x\": [6.19], \"y\": [2141.320068359375]}, {\"marker\": {\"size\": [15]}, \"name\": \"5/12 0/6\", \"type\": \"scatter\", \"x\": [6.22], \"y\": [2126.72998046875]}, {\"name\": \"3/12 0/6\", \"type\": \"scatter\", \"x\": [6.23, 6.24, 6.25], \"y\": [2131.239990234375, 2161.510009765625, 2112.3701171875]}, {\"name\": \"2/12 0/6\", \"type\": \"scatter\", \"x\": [6.26, 6.29, 6.3], \"y\": [2134.64990234375, 2093.47998046875, 2108.330078125]}, {\"mode\": \"markers+text\", \"name\": \"Weight #1\", \"text\": [\"30\"], \"type\": \"scatter\", \"x\": [6.03], \"y\": [2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #2\", \"text\": [\"15\"], \"type\": \"scatter\", \"x\": [6.07], \"y\": [2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #3\", \"text\": [\"10\", \"10\"], \"type\": \"scatter\", \"x\": [6.11, 6.21], \"y\": [2220, 2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #4\", \"text\": [\"0\", \"0\"], \"type\": \"scatter\", \"x\": [6.15, 6.28], \"y\": [2220, 2220, 2220]}, {\"line\": {\"color\": \"Black\"}, \"name\": \"Close\", \"type\": \"scatter\", \"x\": [6.01, 6.02, 6.03, 6.04, 6.05, 6.08, 6.09, 6.1, 6.11, 6.12, 6.15, 6.16, 6.17, 6.18, 6.19, 6.22, 6.23, 6.24, 6.25, 6.26, 6.29, 6.3], \"y\": [2065.080078125, 2087.18994140625, 2147.0, 2151.179931640625, 2181.8701171875, 2184.2900390625, 2188.919921875, 2195.68994140625, 2176.780029296875, 2132.300048828125, 2030.8199462890625, 2138.050048828125, 2141.050048828125, 2133.47998046875, 2141.320068359375, 2126.72998046875, 2131.239990234375, 2161.510009765625, 2112.3701171875, 2134.64990234375, 2093.47998046875, 2108.330078125]}, {\"name\": \"11/12 2/6\", \"type\": \"scatter\", \"x\": [6.01, 6.02], \"y\": [2065.080078125, 2087.18994140625]}, {\"name\": \"10/12 0/6\", \"type\": \"scatter\", \"x\": [6.03, 6.04, 6.05, 6.08], \"y\": [2147.0, 2151.179931640625, 2181.8701171875, 2184.2900390625]}, {\"marker\": {\"size\": [15]}, \"name\": \"9/12 0/6\", \"type\": \"scatter\", \"x\": [6.09], \"y\": [2188.919921875]}, {\"marker\": {\"size\": [15]}, \"name\": \"8/12 0/6\", \"type\": \"scatter\", \"x\": [6.1], \"y\": [2195.68994140625]}, {\"name\": \"6/12 0/6\", \"type\": \"scatter\", \"x\": [6.11, 6.12, 6.15, 6.16, 6.17], \"y\": [2176.780029296875, 2132.300048828125, 2030.8199462890625, 2138.050048828125, 2141.050048828125]}, {\"marker\": {\"size\": [15]}, \"name\": \"7/12 0/6\", \"type\": \"scatter\", \"x\": [6.18], \"y\": [2133.47998046875]}, {\"marker\": {\"size\": [15]}, \"name\": \"6/12 0/6\", \"type\": \"scatter\", \"x\": [6.19], \"y\": [2141.320068359375]}, {\"marker\": {\"size\": [15]}, \"name\": \"5/12 0/6\", \"type\": \"scatter\", \"x\": [6.22], \"y\": [2126.72998046875]}, {\"name\": \"3/12 0/6\", \"type\": \"scatter\", \"x\": [6.23, 6.24, 6.25], \"y\": [2131.239990234375, 2161.510009765625, 2112.3701171875]}, {\"name\": \"2/12 0/6\", \"type\": \"scatter\", \"x\": [6.26, 6.29, 6.3], \"y\": [2134.64990234375, 2093.47998046875, 2108.330078125]}, {\"mode\": \"markers+text\", \"name\": \"Weight #1\", \"text\": [\"30\"], \"type\": \"scatter\", \"x\": [6.03], \"y\": [2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #2\", \"text\": [\"15\"], \"type\": \"scatter\", \"x\": [6.07], \"y\": [2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #3\", \"text\": [\"10\", \"10\"], \"type\": \"scatter\", \"x\": [6.11, 6.21], \"y\": [2220, 2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #4\", \"text\": [\"0\", \"0\"], \"type\": \"scatter\", \"x\": [6.15, 6.28], \"y\": [2220, 2220, 2220]}, {\"line\": {\"color\": \"Black\"}, \"name\": \"Close\", \"type\": \"scatter\", \"x\": [6.01, 6.02, 6.03, 6.04, 6.05, 6.08, 6.09, 6.1, 6.11, 6.12, 6.15, 6.16, 6.17, 6.18, 6.19, 6.22, 6.23, 6.24, 6.25, 6.26, 6.29, 6.3], \"y\": [2065.080078125, 2087.18994140625, 2147.0, 2151.179931640625, 2181.8701171875, 2184.2900390625, 2188.919921875, 2195.68994140625, 2176.780029296875, 2132.300048828125, 2030.8199462890625, 2138.050048828125, 2141.050048828125, 2133.47998046875, 2141.320068359375, 2126.72998046875, 2131.239990234375, 2161.510009765625, 2112.3701171875, 2134.64990234375, 2093.47998046875, 2108.330078125]}, {\"name\": \"11/12 2/6\", \"type\": \"scatter\", \"x\": [6.01, 6.02], \"y\": [2065.080078125, 2087.18994140625]}, {\"name\": \"10/12 0/6\", \"type\": \"scatter\", \"x\": [6.03, 6.04, 6.05, 6.08], \"y\": [2147.0, 2151.179931640625, 2181.8701171875, 2184.2900390625]}, {\"marker\": {\"size\": [15]}, \"name\": \"9/12 0/6\", \"type\": \"scatter\", \"x\": [6.09], \"y\": [2188.919921875]}, {\"marker\": {\"size\": [15]}, \"name\": \"8/12 0/6\", \"type\": \"scatter\", \"x\": [6.1], \"y\": [2195.68994140625]}, {\"name\": \"6/12 0/6\", \"type\": \"scatter\", \"x\": [6.11, 6.12, 6.15, 6.16, 6.17], \"y\": [2176.780029296875, 2132.300048828125, 2030.8199462890625, 2138.050048828125, 2141.050048828125]}, {\"marker\": {\"size\": [15]}, \"name\": \"7/12 0/6\", \"type\": \"scatter\", \"x\": [6.18], \"y\": [2133.47998046875]}, {\"marker\": {\"size\": [15]}, \"name\": \"6/12 0/6\", \"type\": \"scatter\", \"x\": [6.19], \"y\": [2141.320068359375]}, {\"marker\": {\"size\": [15]}, \"name\": \"5/12 0/6\", \"type\": \"scatter\", \"x\": [6.22], \"y\": [2126.72998046875]}, {\"name\": \"3/12 0/6\", \"type\": \"scatter\", \"x\": [6.23, 6.24, 6.25], \"y\": [2131.239990234375, 2161.510009765625, 2112.3701171875]}, {\"name\": \"2/12 0/6\", \"type\": \"scatter\", \"x\": [6.26, 6.29, 6.3], \"y\": [2134.64990234375, 2093.47998046875, 2108.330078125]}, {\"mode\": \"markers+text\", \"name\": \"Weight #1\", \"text\": [\"30\"], \"type\": \"scatter\", \"x\": [6.03], \"y\": [2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #2\", \"text\": [\"15\"], \"type\": \"scatter\", \"x\": [6.07], \"y\": [2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #3\", \"text\": [\"10\", \"10\"], \"type\": \"scatter\", \"x\": [6.11, 6.21], \"y\": [2220, 2220]}, {\"mode\": \"markers+text\", \"name\": \"Weight #4\", \"text\": [\"0\", \"0\"], \"type\": \"scatter\", \"x\": [6.15, 6.28], \"y\": [2220, 2220, 2220]}],\n",
       "                        {\"shapes\": [{\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.04, \"x1\": 6.04, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.1, \"x1\": 6.1, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.12, \"x1\": 6.12, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.19, \"x1\": 6.19, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.24, \"x1\": 6.24, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.04, \"x1\": 6.04, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.1, \"x1\": 6.1, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.12, \"x1\": 6.12, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.19, \"x1\": 6.19, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.24, \"x1\": 6.24, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.04, \"x1\": 6.04, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.1, \"x1\": 6.1, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.12, \"x1\": 6.12, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.19, \"x1\": 6.19, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.24, \"x1\": 6.24, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.04, \"x1\": 6.04, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.1, \"x1\": 6.1, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.12, \"x1\": 6.12, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.19, \"x1\": 6.19, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}, {\"line\": {\"color\": \"Black\", \"dash\": \"dot\", \"width\": 1}, \"type\": \"line\", \"x0\": 6.24, \"x1\": 6.24, \"xref\": \"x\", \"y0\": 0, \"y1\": 2250, \"yref\": \"y\"}], \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"title\": {\"text\": \"Kospi Close\"}, \"xaxis\": {\"dtick\": 0.01, \"tick0\": 6.01, \"tickmode\": \"linear\", \"title\": {\"text\": \"days\"}}, \"yaxis\": {\"range\": [2000, 2250], \"title\": {\"text\": \"Price\"}}},\n",
       "                        {\"responsive\": true}\n",
       "                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('158a6a8f-ae91-428d-9078-ffe8d4f850a5');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })\n",
       "                };\n",
       "                });\n",
       "            </script>\n",
       "        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly.offline as offline\n",
    "import plotly.graph_objs as go \n",
    "offline.init_notebook_mode(connected=True)\n",
    "\n",
    "\n",
    "\n",
    "# Scatter graph\n",
    "\n",
    "fig.add_trace(go.Scatter(x=Kospi.index,y=Kospi.Close,name=\"Close\",line=dict(color='Black')))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[0:2],y=Kospi.Close.iloc[:2], name=\"11/12 2/6\"))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[2:6],y=Kospi.Close.iloc[2:6], name=\"10/12 0/6\"))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[6:7],y=Kospi.Close.iloc[6:7], name=\"9/12 0/6\",marker=dict(size=[15])))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[7:8],y=Kospi.Close.iloc[7:8], name=\"8/12 0/6\",marker=dict(size=[15])))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[8:13],y=Kospi.Close.iloc[8:13], name=\"6/12 0/6\"))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[13:14],y=Kospi.Close.iloc[13:14], name=\"7/12 0/6\",marker=dict(size=[15])))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[14:15],y=Kospi.Close.iloc[14:15], name=\"6/12 0/6\",marker=dict(size=[15])))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[15:16],y=Kospi.Close.iloc[15:16], name=\"5/12 0/6\",marker=dict(size=[15])))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[16:19],y=Kospi.Close.iloc[16:19], name=\"3/12 0/6\"))\n",
    "fig.add_trace(go.Scatter(x=Kospi.index[19:22],y=Kospi.Close.iloc[19:22], name=\"2/12 0/6\"))\n",
    "\n",
    "#MAKE VERTICAL LINE\n",
    "fig.add_shape(\n",
    "        # Line Vertical\n",
    "        dict(\n",
    "            type=\"line\",\n",
    "            x0=6.04,\n",
    "            y0=0,\n",
    "            x1=6.04,\n",
    "            y1=2250,\n",
    "            line=dict(\n",
    "                color=\"Black\",\n",
    "                dash=\"dot\",\n",
    "                width=1\n",
    "            )))\n",
    "\n",
    "fig.add_shape(\n",
    "        # Line Vertical\n",
    "        dict(\n",
    "            type=\"line\",\n",
    "            x0=6.10,\n",
    "            y0=0,\n",
    "            x1=6.10,\n",
    "            y1=2250,\n",
    "            line=dict(\n",
    "                color=\"Black\",\n",
    "                dash=\"dot\",\n",
    "                width=1\n",
    "            )))\n",
    "fig.add_shape(\n",
    "        # Line Vertical\n",
    "        dict(\n",
    "            type=\"line\",\n",
    "            x0=6.12,\n",
    "            y0=0,\n",
    "            x1=6.12,\n",
    "            y1=2250,\n",
    "            line=dict(\n",
    "                color=\"Black\",\n",
    "                dash=\"dot\",\n",
    "                width=1\n",
    "            )))\n",
    "fig.add_shape(\n",
    "        # Line Vertical\n",
    "        dict(\n",
    "            type=\"line\",\n",
    "            x0=6.19,\n",
    "            y0=0,\n",
    "            x1=6.19,\n",
    "            y1=2250,\n",
    "            line=dict(\n",
    "                color=\"Black\",\n",
    "                dash=\"dot\",\n",
    "                width=1\n",
    "            )))\n",
    "fig.add_shape(\n",
    "        # Line Vertical\n",
    "        dict(\n",
    "            type=\"line\",\n",
    "            x0=6.24,\n",
    "            y0=0,\n",
    "            x1=6.24,\n",
    "            y1=2250,\n",
    "            line=dict(\n",
    "                color=\"Black\",\n",
    "                dash=\"dot\",\n",
    "                width=1\n",
    "            )))\n",
    "\n",
    "#ANNOTATION\n",
    "\n",
    "fig.add_trace(go.Scatter(\n",
    "    x=[6.03],\n",
    "    y=[2220],\n",
    "    mode=\"markers+text\",\n",
    "    name=\"Weight #1\",\n",
    "    text=[\"30\"],\n",
    "    \n",
    "))\n",
    "fig.add_trace(go.Scatter(\n",
    "    x=[6.07],\n",
    "    y=[2220],\n",
    "    mode=\"markers+text\",\n",
    "    name=\"Weight #2\",\n",
    "    text=[\"15\"],\n",
    "    \n",
    "))\n",
    "fig.add_trace(go.Scatter(\n",
    "    x=[6.11,6.21],\n",
    "    y=[2220,2220],\n",
    "    mode=\"markers+text\",\n",
    "    name=\"Weight #3\",\n",
    "    text=[\"10\",\"10\"],\n",
    "          ))          \n",
    "fig.add_trace(go.Scatter(\n",
    "    x=[6.15,6.28],\n",
    "    y=[2220,2220,2220],\n",
    "    mode=\"markers+text\",\n",
    "    name=\"Weight #4\",\n",
    "    text=[\"0\",\"0\"]   \n",
    "))\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "fig.update_shapes(dict(xref='x', yref='y'))\n",
    "fig.update_layout(title='Kospi Close',\n",
    "                 xaxis_title='days'\n",
    "                 , yaxis_title='Price',\n",
    "                   xaxis = dict(\n",
    "                           tickmode = 'linear',\n",
    "                           tick0 = 6.01,\n",
    "                           dtick = 0.01),\n",
    "                 yaxis=dict(range=(2000,2250),\n",
    "                 \n",
    "           \n",
    "                 ))\n",
    "fig.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
