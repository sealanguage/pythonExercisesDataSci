{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter grades to calculate mean/average grades. tyep e to exit\n",
      " enter grades 3.5\n",
      " enter grades 2.2\n",
      " enter grades 4.0\n",
      " enter grades 1.1\n",
      " enter grades e\n",
      "grades:  [3.5, 2.2, 4.0, 1.1]\n",
      "Average class grade is:  2.6999999999999997\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter grades to calculate mean/average grades. tyep e to exit\")\n",
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
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## "
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
