{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "pset2.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMesRssz4skTykId0NvYhNM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/liamlewis1030/datascience/blob/main/pset2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "79fdlapYM8cp",
        "outputId": "28469436-bf39-4ad7-9c9b-9d00e52dbf85"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Average of a1 = 5.2\n"
          ]
        }
      ],
      "source": [
        "def average(l): \n",
        "    sum=0\n",
        "    for i in l:\n",
        "        sum=sum+i\n",
        "    avg = sum / len(l) \n",
        "    return avg\n",
        "  \n",
        "a1 = [1,6,3,9,7] \n",
        "average(a1) \n",
        "  \n",
        "print(\"Average of a1 =\", average(a1))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a1 = [3,0]\n",
        "a2 = [6,1,7]\n",
        "def common(x,y):\n",
        "    w=False\n",
        "    for a in x:\n",
        "        for b in y:\n",
        "            print(a,b)\n",
        "            if a == b:\n",
        "                print(\"Common element!\")\n",
        "                w=True\n",
        "    return w\n",
        "common(a1,a2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3tRtkucQNJH8",
        "outputId": "6e89ce3c-febe-40eb-8864-17b0655d68f4"
      },
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 6\n",
            "3 1\n",
            "3 7\n",
            "0 6\n",
            "0 1\n",
            "0 7\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a1 = [3,7,12,16,-4,6,0,1,0]\n",
        "def zerooo(x):\n",
        "    for a in x:\n",
        "        if a != 0:\n",
        "            print(a)\n",
        "        if a==0:\n",
        "            print('zerooo')\n",
        "zerooo(a1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pCTii0kBNJ6u",
        "outputId": "6c87d365-8d74-4cb5-9e67-763a57e68863"
      },
      "execution_count": 95,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "7\n",
            "12\n",
            "16\n",
            "-4\n",
            "6\n",
            "zerooo\n",
            "1\n",
            "zerooo\n"
          ]
        }
      ]
    }
  ]
}