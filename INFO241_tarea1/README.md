# BioInfomatica_INFO241 Junio-2023
#Tarea 1 
#Grupo 
	- Andrade , Jorge		- jorge.andrade01@alumnos.uach.cl
	- Fuentes , Sebastian	- sebastian.fuentes02@alumnos.uach.cl
	- Pezo 	  ,	Juan Pablo	- juan.pezo@alumnos.uach.cl
	- Pinilla ,	Claudio		- claudio.pinilla@alumnos.uach.cl


#Comentarios de la tarea 
-
- En la parte 2 (splitFasta.sh)
	- Se menciona que al dividir el doc.fasta principal, desde la descripcion (Primeros 5 char y ultimos 5, sin incluir los no validos)se despliguen los nombres para los siguientes .fasta 
	- Al realizar esto Ocurre un problema cuando coinciden los nombres. Ocacionando que se omita uno de los dos documentos .fasta
	- Para ello se realizo agrego el identificados comun NR que al dividir cada archivo incrementa su valor y lo agrega al inicio del nombre (Impidiendo que ocacione duplicidad)
	
	-> Se realizo una prueba de Script (splitFasta.sh) con los siguientes .fasta
		-Se descargaron:
		https://www.ncbi.nlm.nih.gov/nuccore/NC_077229.1?report=fasta
		https://www.ncbi.nlm.nih.gov/nuccore/NC_072436.1?report=fasta	
		https://www.ncbi.nlm.nih.gov/nuccore/NC_071448.1?report=fasta
		https://www.ncbi.nlm.nih.gov/nuccore/NC_060939.1?report=fasta
		https://www.ncbi.nlm.nih.gov/nuccore/NC_060940.1?report=fasta
		https://www.ncbi.nlm.nih.gov/nuccore/NC_073234.1?report=fasta
		https://www.ncbi.nlm.nih.gov/nuccore/NG_017013.2?report=fasta&from=5001&to=24149
		-Se realizo un cat <seq1.fasta> <seq2.fasta> <seq3.fasta> <seq4.fasta> <seq5.fasta> <seq6.fasta> <seq7.fasta>> multiSeq.fasta
		donde coincide el 4to con el 5to (Homo sapiens chromosome 16 y Homo sapiens chromosome 16) generando el mismo nombre NC_0603v2.0.fasta (Causando duplicidad, por entre se argumenta el colocar Indice)
