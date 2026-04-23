{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO36eNY6WtaMc2Al4W1495A",
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
        "<a href=\"https://colab.research.google.com/github/UFPAJoaoVictorIA/trabalho-Extra-UFPA-ARQ.ORG.COMP/blob/UFPAJoaoVictorIA-patch-2/Utilis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "t-ohpni9ORVs"
      },
      "outputs": [],
      "source": [
        "from utils import quantizacao\n",
        "\n",
        "niveis = int(input(\"Digite os níveis: \"))\n",
        "bits, combinacoes = quantizacao(niveis)\n",
        "\n",
        "print(\"Bits:\", bits)\n",
        "print(\"Combinações:\")\n",
        "for c in combinacoes:\n",
        "    print(c)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from utils import decimal_para_binario\n",
        "\n",
        "num = int(input(\"Digite um número decimal: \"))\n",
        "print(decimal_para_binario(num))"
      ],
      "metadata": {
        "id": "GHX8SDH4O8uk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from utils import decimal_fracionario_para_binario, binario_para_decimal\n",
        "\n",
        "num = float(input(\"Número decimal: \"))\n",
        "b = decimal_fracionario_para_binario(num)\n",
        "\n",
        "print(\"Binário:\", b)\n",
        "print(\"Decimal:\", binario_para_decimal(b))"
      ],
      "metadata": {
        "id": "eBxGRkegPDRn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from utils import *\n",
        "\n",
        "valor = input(\"Digite o número: \")\n",
        "base = int(input(\"Base (8 ou 16): \"))\n",
        "\n",
        "binario, decimal = qualquer_para_decimal(valor, base)\n",
        "\n",
        "print(\"Binário:\", binario)\n",
        "print(\"Decimal:\", decimal)"
      ],
      "metadata": {
        "id": "YC82JlpRPDga"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}