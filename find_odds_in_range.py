{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter first number in range > 32\n",
      "enter last number in range > 64\n",
      "enter the nth odd number > 10\n",
      "nth_odd_num =  51\n"
     ]
    }
   ],
   "source": [
    "first_number = int(input(\"enter first number in range > \"))\n",
    "last_number = int(input(\"enter last number in range > \"))\n",
    "nth_odd_num  = int(input(\"enter the nth odd number > \"))\n",
    "count = 0  # count the odd numbers\n",
    "actual_nth_odd_num = 0\n",
    "\n",
    "for number in range(first_number, last_number + 1) :\n",
    "    if number %2 != 0 :\n",
    "        count = count + 1\n",
    "        if count == nth_odd_num :\n",
    "            actual_nth_odd_num = number\n",
    "            break\n",
    "                \n",
    "print(\"nth_odd_num = \", actual_nth_odd_num)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
