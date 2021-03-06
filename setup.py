import setuptools


setuptools.setup(

    name="fastq2matrix",
    version="0.1.2",
    packages=["fastq2matrix"],
    license="MIT",
    long_description="Utilities to get from fastq files to a variant matrix",
    scripts= [
        'scripts/fastq2vcf.py',
        'scripts/merge_vcfs.py',
        'scripts/setGT.py',
        'scripts/vcf2fasta.py',
		'scripts/vcf2dist.py',
        'scripts/filter_merged_vcf.py',
        'scripts/vcf2matrix.py',
        'scripts/merge_bams.py',
        'scripts/ancestral_reconstruction.py'
        ],

)
