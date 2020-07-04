{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-3-5d1e93a3e16f>, line 20)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-3-5d1e93a3e16f>\"\u001b[0;36m, line \u001b[0;32m20\u001b[0m\n\u001b[0;31m    print(\"Average class grade is: \", average\u001b[0m\n\u001b[0m                                             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "#    print(\"Enter grades to calculate mean/average grades. tyep e to exit\")\n",
    "\n",
    "# create an empty list\n",
    "grades = []\n",
    "sum = 0\n",
    "\n",
    "while( True ) :\n",
    "    grade = input(\" enter grades \")\n",
    "    if grade == \"e\" :\n",
    "        break\n",
    "    else :\n",
    "        grade = float(grade)\n",
    "        grades.append(grade)\n",
    "print(\"grades: \", grades)\n",
    "        \n",
    "\n",
    "for grade in grades :\n",
    "    sum = sum + grade\n",
    "average = sum /len(grades)\n",
    "print(\"Average class grade is: \", average"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " enter grades 3.2\n",
      " enter grades 2.1\n",
      " enter grades 3.7\n",
      " enter grades 3.3\n",
      " enter grades 1.0\n",
      " enter grades e\n",
      "grades:  [3.2, 2.1, 3.7, 3.3, 1.0]\n",
      "Average class grade is:  2.66\n"
     ]
    }
   ],
   "source": [
    "#    print(\"Enter grades to calculate mean/average grades. tyep e to exit\")\n",
    "\n",
    "# create an empty list\n",
    "grades = []\n",
    "sum = 0\n",
    "\n",
    "while( True ) :\n",
    "    grade = input(\" enter grades \")\n",
    "    if grade == \"e\" :\n",
    "        break\n",
    "    else :\n",
    "        grade = float(grade)\n",
    "        grades.append(grade)\n",
    "print(\"grades: \", grades)\n",
    "        \n",
    "\n",
    "for grade in grades :\n",
    "    sum = sum + grade\n",
    "average = sum /len(grades)\n",
    "print(\"Average class grade is: \", average)"
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
