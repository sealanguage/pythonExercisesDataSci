{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_interest(balance, interest, days) :\n",
    "    interest_amount = balance * (interest / 100) * (days/365)\n",
    "    return interest_amount"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'days' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-0107e6cca253>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mcalculate_interest\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m2000\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m30\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-1-bc94be9d9a28>\u001b[0m in \u001b[0;36mcalculate_interest\u001b[0;34m(balance, interest, day)\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mcalculate_interest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbalance\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minterest\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mday\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m     \u001b[0minterest_amount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbalance\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0minterest\u001b[0m \u001b[0;34m/\u001b[0m \u001b[0;36m100\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mdays\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0;36m365\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0minterest_amount\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'days' is not defined"
     ]
    }
   ],
   "source": [
    "calculate_interest (2000, 3, 30)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_interest(balance, interest, days) :\n",
    "    interest_amount = balance * (interest / 100) * (days/365)\n",
    "    return interest_amount"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.36986301369863"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calculate_interest (50, 10, 100)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_interest_curr(balance, interest, days) :\n",
    "    \"\"\"\n",
    "    1. Balance: Amount on which balance needs to be calculated\n",
    "    2. Interest: annual interest in percentage\n",
    "    3. Days: numver of days since the beginning of the year\n",
    "    \"\"\"\n",
    "\n",
    "    interest_amount = balance * (interest / 100) * (days/365)\n",
    "    return interest_amount"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "def calculate_interest_curr(balance, interest, days) :\n",
    "    \"\"\"\n",
    "    1. Balance: Amount on which balance needs to be calculated\n",
    "    2. Interest: annual interest in percentage\n",
    "    3. Days: numver of days since the beginning of the year\n",
    "    \"\"\"\n",
    "\n",
    "    interest_amount = balance * (interest / 100) * (days/365)\n",
    "    return interest_amount"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "calculate_interest_curr"
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
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
