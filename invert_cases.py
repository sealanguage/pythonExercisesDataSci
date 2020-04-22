{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "input a string: HackerRank.com presents \"Pythonist 2\".\n",
      "hACKERrANKCOM PRESENTS pYTHONIST 2"
     ]
    }
   ],
   "source": [
    "#   Pythonist 2  to  pYTHONIST 2\n",
    "#   HackerRank.com presents \"Pythonist 2\".\n",
    "\n",
    "# swapcase()\n",
    "\n",
    "str = input( \"input a string: \")\n",
    "\n",
    "for i in str :\n",
    "    if i.islower() :\n",
    "        print(i.upper(), end = '')\n",
    "    if i.isupper() :\n",
    "        print(i.lower(), end = '')\n",
    "    if i.isnumeric() :\n",
    "        print(i, end = '')\n",
    "    if i.isspace() :\n",
    "        print(i, end = '')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'pYTHONIST 2'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "B\n"
     ]
    }
   ],
   "source": [
    "a = 2\n",
    "b = 330\n",
    "print(\"A\") if a > b else print(\"B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-26-dfbe0077bbd3>, line 8)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-26-dfbe0077bbd3>\"\u001b[0;36m, line \u001b[0;32m8\u001b[0m\n\u001b[0;31m    print(i.lower()) if i.isupper else i.isupper() print(i.upper())\u001b[0m\n\u001b[0m                                                   ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#   Pythonist 2  to  pYTHONIST 2\n",
    "\n",
    "str = input( \"input a string: \")\n",
    "# print(\"str\")\n",
    "\n",
    "for i in str :\n",
    "#     if i.islower :\n",
    "        print(i.lower()) if i.isupper else i.isupper() print(i.upper())\n",
    "#     if i.isupper :\n",
    "#         print(i.lower())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'library'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-52-8da9838c1322>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# swapcase()\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mlibrary\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0mstr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m \u001b[0;34m\"input a string: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'library'"
     ]
    }
   ],
   "source": [
    "#   Pythonist 2  to  pYTHONIST 2\n",
    "#   HackerRank.com presents \"Pythonist 2\".\n",
    "\n",
    "\n",
    "str = input( \"input a string: \")\n",
    "\n",
    "for i in str :\n",
    "    print(i.swapcase(), end = '')\n",
    "    if i == str.punctuation : \n",
    "        print(i, end = '')\n",
    "    \n",
    "    "
   ]
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
