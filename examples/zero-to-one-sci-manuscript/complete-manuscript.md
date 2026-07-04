# DRK1 Supports ABA-Induced Stomatal Closure in Arabidopsis Guard Cells

Lin Chen1, Mei Zhang1, Arun Patel2, and Hua Li1*

1. Department of Plant Biology, Example University, Shanghai, China
2. Center for Plant Stress Biology, Example Institute, Singapore

*Correspondence: hua.li@example.edu

## Abstract

Abscisic acid (ABA) promotes stomatal closure during water stress, yet the kinase-level regulators that tune the amplitude of guard-cell responses remain incompletely defined. Here, we characterize DRK1, a candidate Arabidopsis kinase identified from a guard-cell ABA-response screen. Loss of DRK1 did not alter basal stomatal aperture but strongly attenuated ABA-induced closure. After 10 uM ABA treatment for 2 h, wild-type stomata narrowed from 4.82 +/- 0.13 um to 2.08 +/- 0.09 um, whereas drk1-1 stomata remained wider at 3.61 +/- 0.12 um. Native-promoter complementation restored most of the ABA response, supporting a DRK1-linked contribution to the phenotype. DRK1 disruption also reduced ABA-induced guard-cell ROS accumulation and attenuated induction of selected ABA-responsive marker transcripts. These results indicate that DRK1 is required for the full guard-cell response to ABA under the tested conditions. Because direct substrate, epistasis, and biochemical data are not yet available, we interpret DRK1 as a positive contributor to ABA responsiveness rather than as a defined upstream regulator of ROS production.

## Significance Statement

ABA-induced stomatal closure is central to plant water-stress adaptation. This study identifies DRK1 as a positive contributor to the full guard-cell ABA response and links mutant phenotype, genetic complementation, ROS imaging, and ABA-responsive marker expression into a bounded model of kinase-associated stomatal regulation.

## Keywords

abscisic acid; Arabidopsis; guard cell; protein kinase; reactive oxygen species; stomatal closure

## Introduction

Stomata coordinate carbon dioxide uptake with transpirational water loss, making guard-cell regulation a key determinant of plant performance under fluctuating water availability. ABA has long been recognized as a central drought-associated signal that promotes stomatal closure and helps limit water loss [1,2]. Genetic, electrophysiological, and biochemical studies have shown that guard-cell ABA responses integrate ion flux, calcium signaling, ROS production, protein phosphorylation, and transcriptional regulation [1-4]. This mature literature establishes stomatal closure as a tractable system for connecting hormone perception to cell-type-specific physiological output.

The core ABA signaling module is built around PYR/PYL/RCAR receptors, PP2C phosphatases, and SnRK2 kinases [2,5,6]. In guard cells, OST1/SnRK2.6 is required for ABA-regulated stomatal movement and acts upstream of several downstream outputs [7]. ROS production by NADPH oxidases, including AtrbohD and AtrbohF, contributes to ABA-dependent calcium-channel activation and stomatal closure [3,4]. Anion channels such as SLAC1 provide a further link between kinase signaling and ion efflux during closure [8,9]. Together, these studies define a core framework in which phosphorylation events, ROS, calcium, and ion-channel regulation converge to reduce stomatal aperture.

Despite this framework, several levels of regulation remain unresolved. First, many kinase candidates may modulate the strength, timing, or context dependence of ABA responses without being core pathway components. Second, mutant phenotypes are often interpreted too quickly as direct mechanism, even when they only establish contribution to a response. Third, guard-cell phenotypes frequently require several evidence layers--genetic specificity, physiological output, cellular signaling readout, and transcript or molecular context--before a manuscript can make a defensible claim. Distinguishing contribution from direct pathway placement is therefore essential for interpreting newly identified ABA-response regulators.

DRK1 was selected as a candidate guard-cell regulator because preliminary expression analysis and mutant screening suggested altered ABA responsiveness. However, whether DRK1 contributes to ABA-induced stomatal closure, whether the phenotype is genetically linked to DRK1 disruption, and whether DRK1 affects known ABA-associated outputs remained unknown. We addressed these questions using stomatal aperture assays, native-promoter complementation, guard-cell ROS imaging, and ABA-responsive marker-gene expression analysis. We show that DRK1 disruption reduces ABA-induced stomatal closure, that DRK1 complementation restores most of the response, and that DRK1 affects ABA-induced ROS accumulation and selected ABA-responsive transcripts. The resulting model places DRK1 as a positive contributor to the full guard-cell ABA response while deliberately leaving its precise molecular position unresolved.

## Results

### DRK1 disruption attenuates ABA-induced stomatal closure

We first tested whether DRK1 contributes to ABA-induced stomatal closure by comparing wild-type Col-0 and drk1-1 plants after mock or ABA treatment. Under mock conditions, wild-type and drk1-1 stomata had similar apertures, with mean values of 4.82 +/- 0.13 um and 4.91 +/- 0.14 um, respectively (Fig. 1A and 1B). This baseline similarity was important because it allowed the ABA response to be interpreted independently of constitutive aperture differences. After treatment with 10 uM ABA for 2 h, wild-type stomata narrowed to 2.08 +/- 0.09 um, whereas drk1-1 stomata remained significantly wider at 3.61 +/- 0.12 um (Fig. 1B). A two-way ANOVA detected a significant genotype-by-treatment interaction (P < 0.0001), supporting a specific defect in ABA-induced closure.

To evaluate the robustness of this phenotype, we examined both distribution-level and replicate-level behavior. Mock-treated wild-type and drk1-1 aperture distributions largely overlapped, whereas ABA-treated drk1-1 stomata showed a right-shifted distribution relative to ABA-treated wild type (Fig. 1C). Across three independent biological replicates, each containing 60 measured stomata per genotype and treatment, the ABA-induced closure index was reduced by 58% in drk1-1 compared with wild type (Fig. 1D). These controls, replicate structure, and distributional data support the conclusion that DRK1 is required for the full ABA-induced stomatal closure response under the tested conditions. Because a loss-of-function phenotype alone cannot establish direct pathway placement, we next asked whether the phenotype could be genetically complemented.

### Native-promoter DRK1 complementation partially restores ABA responsiveness

To test whether the impaired closure phenotype was linked to DRK1 disruption, we generated a complementation line expressing DRK1 under its native promoter in the drk1-1 background. Quantitative RT-PCR showed that DRK1 transcript abundance in the complementation line reached 0.87 +/- 0.08-fold of the wild-type level (Fig. 2A), indicating that the transgene restored DRK1 expression without strong overexpression. Under mock conditions, stomatal aperture in the complementation line remained comparable to wild type and drk1-1, consistent with DRK1 acting primarily under ABA treatment in this assay.

After ABA treatment, stomatal aperture in the complementation line decreased to 2.46 +/- 0.10 um, significantly narrower than drk1-1 and moderately wider than wild type (Fig. 2B). The partial rescue was reproduced across three independent experiments and recovered approximately 75% of the ABA-induced closure defect. This result strengthens the genetic specificity of the drk1-1 phenotype, but it also places an important boundary on the claim: DRK1 complementation supports a DRK1-linked contribution to ABA responsiveness, not complete sufficiency for all pathway outputs. Having established phenotype specificity, we then examined whether DRK1 disruption affected a known cellular feature of guard-cell ABA signaling.

### DRK1 disruption reduces ABA-induced ROS accumulation in guard cells

ABA-induced ROS accumulation is a conserved component of guard-cell ABA signaling and has been linked to calcium-channel activation and stomatal closure [3,4]. We therefore measured ROS production using H2DCF-DA fluorescence in epidermal peels after mock or ABA treatment. In wild-type guard cells, ABA increased normalized ROS fluorescence 2.68 +/- 0.18-fold relative to mock (Fig. 3A and 3B). In drk1-1, ABA increased fluorescence only 1.42 +/- 0.11-fold, indicating a strong attenuation of the ROS response. The complementation line showed a substantially restored response of 2.21 +/- 0.15-fold (Fig. 3B).

Several controls supported the reliability of this assay. All genotypes were imaged under identical acquisition settings, fluorescence values were normalized within each biological replicate, and mock-treated samples showed no genotype-dependent elevation in baseline fluorescence. The concordance between impaired closure and reduced ABA-induced ROS accumulation suggests that DRK1 affects an ABA-associated cellular output. However, the data do not establish whether DRK1 acts upstream of ROS production, downstream of ROS, or in a parallel branch that modulates both ROS readout and closure capacity. We therefore treated the ROS phenotype as pathway-associated evidence and next tested whether DRK1 disruption also influenced ABA-responsive transcript output.

### DRK1 affects selected ABA-responsive marker transcripts

To determine whether DRK1 disruption affects ABA-responsive molecular outputs beyond guard-cell aperture and ROS fluorescence, we measured expression of RD29B, RAB18, and ABI5 after 3 h of ABA treatment. In wild-type seedlings, RD29B, RAB18, and ABI5 increased 6.4 +/- 0.7-fold, 5.8 +/- 0.6-fold, and 3.1 +/- 0.4-fold, respectively (Fig. 4A). In drk1-1, induction of the same transcripts was reduced to 3.2 +/- 0.4-fold, 2.7 +/- 0.3-fold, and 1.8 +/- 0.2-fold. The complementation line partially restored induction for all three markers (Fig. 4A).

These marker-gene data extend the DRK1 phenotype to a broader ABA-responsive output, but they are interpreted conservatively. Because the assay was performed in whole seedlings, it cannot prove guard-cell-specific transcriptional regulation. It does, however, show that the drk1-1 defect is not limited to a single aperture measurement and is accompanied by attenuated ABA-associated molecular responses. Together with the stomatal and ROS results, these data support a model in which DRK1 contributes to the full amplitude of the ABA response.

### DRK1 contributes to a bounded ABA-response model

The combined evidence supports a working model in which DRK1 is a positive contributor to ABA-induced stomatal closure (Fig. 5). The genetic phenotype establishes the physiological requirement, complementation supports specificity, ROS imaging links DRK1 to a known guard-cell ABA-associated output, and marker-gene analysis provides additional molecular context. The model remains bounded: DRK1 is not assigned to a specific step upstream of ROS or ion-channel activation until pathway-ordering, substrate, or biochemical evidence is available.

This model figure therefore functions as a synthesis rather than as new evidence. It records the supported chain from DRK1 disruption to reduced ABA responsiveness and highlights the unresolved pathway position with dashed arrows. Keeping this final result subsection to an evidence summary and boundary statement prevents the manuscript from turning a coherent phenotype story into an unsupported mechanism claim.

## Discussion

This study identifies DRK1 as a positive contributor to ABA-induced stomatal closure in Arabidopsis guard cells. The central result is that drk1-1 mutants show a strong defect in ABA-induced closure while retaining normal basal aperture. Genetic complementation restores most of the response, supporting the interpretation that the phenotype is linked to DRK1 disruption. ROS imaging and marker-gene expression further connect DRK1 to ABA-associated cellular and molecular outputs, producing a bounded but coherent evidence chain.

The DRK1 phenotype fits into a broader ABA signaling framework in which receptor-PP2C-SnRK2 modules, ROS production, calcium signaling, and anion-channel activation coordinate guard-cell closure [1-9]. Within that framework, DRK1 may tune the amplitude or efficiency of ABA signaling rather than serve as an indispensable core component. DRK1 could act upstream of ROS production, downstream of ROS, or in a parallel branch that modulates both ROS accumulation and closure competence. The present data favor a functional connection between DRK1 and ABA-associated ROS output, but epistasis with atrbohD/F or slac1 mutants, kinase-dead complementation, phosphoproteomic analysis, and in vitro substrate assays would be necessary to place DRK1 more precisely.

The study also illustrates the value of layered evidence for newly identified regulators. The aperture assay provides the primary physiological phenotype, complementation supports genetic specificity, ROS imaging gives a pathway-associated cellular readout, and marker-gene expression adds molecular context. Several limitations should be considered: the complementation line restores most but not all ABA responsiveness, the qRT-PCR assay was performed in whole seedlings, and the ROS assay establishes association rather than pathway order. These limits define the next experimental priorities without undermining the central conclusion that DRK1 contributes to the full ABA response.

In summary, DRK1 supports ABA-induced stomatal closure and is associated with ABA-induced ROS and transcript responses. The data establish DRK1 as a positive contributor to guard-cell ABA responsiveness and provide a foundation for future experiments that test whether DRK1 directly interfaces with ROS production, ion-channel regulation, or another branch of the ABA signaling network. For a higher-impact target journal, the most important next step would be to move from contribution to mechanism by identifying a direct DRK1 substrate or genetic interaction.

## Materials and Methods

### Plant material and growth conditions

Arabidopsis thaliana Col-0 was used as the wild-type background. The drk1-1 line was treated as a loss-of-function mutant and was genotyped by PCR before phenotyping. Seeds were surface sterilized in 70% ethanol for 1 min followed by 10% bleach for 8 min, washed five times with sterile water, stratified at 4 C for 3 d, and germinated on half-strength Murashige and Skoog medium. Seven-day-old seedlings were transferred to soil and grown at 22 C under a 16 h light and 8 h dark photoperiod with 120 umol m-2 s-1 light intensity and 60% relative humidity. Four-week-old rosette leaves of similar developmental stage were used for stomatal assays. Plants with visible pathogen symptoms, severe developmental delay, or bolting before harvest were excluded before treatment assignment.

### Complementation line generation

A genomic DRK1 fragment containing 2.1 kb of upstream promoter sequence, the full coding region, and 0.6 kb downstream sequence was cloned into a binary vector using Gibson assembly. The construct was introduced into Agrobacterium tumefaciens strain GV3101 and transformed into drk1-1 plants by floral dip. T1 plants were selected on hygromycin, and homozygous T3 lines were identified by segregation analysis and PCR genotyping. Three independent T3 lines were screened for DRK1 transcript abundance by qRT-PCR; the representative line reported here was selected because its DRK1 expression was closest to the wild-type level.

### Stomatal aperture assay

Fully expanded rosette leaves were harvested 3 h after lights-on to reduce circadian variation. Leaves were floated abaxial side down in opening buffer containing 10 mM MES-KOH pH 6.15, 50 mM KCl, and 10 uM CaCl2 for 2 h under light. Samples were then transferred to fresh opening buffer containing either solvent control or 10 uM ABA for 2 h. ABA was prepared as a 10 mM ethanol stock, and mock-treated samples received the same final ethanol concentration. Epidermal peels were mounted immediately, and bright-field images were acquired using a calibrated 40x objective. Stomatal pore width was measured in ImageJ by an observer blinded to genotype and treatment. Stomata at torn epidermal edges, out-of-focus regions, or visibly damaged guard cells were excluded before measurement. Each biological replicate contained 60 stomata per genotype and treatment, and three independent biological replicates were analyzed.

### ROS imaging

Epidermal peels were incubated in 10 uM H2DCF-DA prepared in opening buffer for 20 min in the dark, washed three times, and treated with mock solution or 10 uM ABA for 20 min. H2DCF-DA was prepared as a DMSO stock immediately before use, and mock samples contained the same final DMSO concentration. Fluorescence images were acquired with the same filter set, exposure time, gain, and illumination intensity across all samples within an experiment. Images containing saturated guard-cell pixels or obvious tissue damage were excluded before genotype decoding. Guard-cell regions of interest were manually segmented in ImageJ, background fluorescence was subtracted from each image, and mean fluorescence was normalized to the mock-treated wild-type mean within each biological replicate. Three independent biological replicates were analyzed.

### Quantitative RT-PCR

Ten-day-old seedlings were treated with mock solution or 10 uM ABA for 3 h. Total RNA was extracted using a plant RNA extraction kit and treated with DNase I. RNA concentration and purity were assessed by spectrophotometry, and samples with A260/A280 ratios outside 1.9-2.1 were not used. First-strand cDNA was synthesized from 1 ug RNA using oligo(dT) primers. qPCR was performed with SYBR Green chemistry using primers for RD29B, RAB18, ABI5, DRK1, and ACTIN2. No-template and no-reverse-transcription controls were included for each primer pair. ACTIN2 was used as the internal control, and primer efficiencies were required to fall between 90% and 110%. Relative expression was calculated by the 2^-Delta Delta Ct method from three biological replicates, each with three technical replicates.

### Statistical analysis

Statistical analyses were performed on biological replicate means unless otherwise stated. Stomatal aperture data were analyzed by two-way ANOVA with genotype and treatment as fixed factors, followed by Tukey's multiple-comparison test. ROS and qRT-PCR data were analyzed by one-way ANOVA among ABA-treated genotypes, followed by Tukey's test. Normality of replicate means was inspected by residual plots, and no data points were removed after statistical inspection. Error bars represent SEM. P values below 0.05 were considered significant. Analyses were performed in R version 4.3.2, and plotting was performed from the same analysis tables used for statistical testing.

## Data Availability

This manuscript is a synthetic example. The numerical data are included in the text, figure legends, and Supplementary Table 1. No real raw microscopy files, sequencing data, or accession records are associated with this example.

## Funding

This synthetic example was not supported by real funding.

## Author Contributions

L.C. and H.L. designed the study. L.C. performed stomatal assays. M.Z. performed ROS imaging and qRT-PCR. A.P. analyzed data and prepared figures. L.C. and H.L. wrote the manuscript with input from all authors.

## Conflict of Interest

The authors declare no competing interests.

## Acknowledgements

We thank members of the Example Plant Biology Group for discussion.

## Figure Legends

### Figure 1. DRK1 disruption attenuates ABA-induced stomatal closure.

(A) Representative bright-field images of stomata from wild-type and drk1-1 leaves after mock or ABA treatment. Scale bar, 10 um. (B) Quantification of stomatal aperture after mock or 10 uM ABA treatment for 2 h. Values are means +/- SEM from three biological replicates, 60 stomata per replicate. (C) Distribution of aperture values in ABA-treated wild type and drk1-1. (D) ABA-induced closure index calculated from replicate means. Different letters indicate P < 0.05 by two-way ANOVA followed by Tukey's test.

### Figure 2. Native-promoter DRK1 complementation partially restores ABA responsiveness.

(A) DRK1 transcript abundance in wild type, drk1-1, and the DRK1 complementation line. Values are normalized to wild type. (B) Stomatal aperture after ABA treatment in wild type, drk1-1, and complemented plants. Values are means +/- SEM from three biological replicates. Different letters indicate P < 0.05 by one-way ANOVA followed by Tukey's test.

### Figure 3. DRK1 disruption reduces ABA-induced ROS accumulation in guard cells.

(A) Representative H2DCF-DA fluorescence images of guard cells after ABA treatment. Scale bar, 20 um. (B) Quantification of normalized fluorescence intensity in mock-treated and ABA-treated samples. Values are means +/- SEM from three biological replicates. Different letters indicate P < 0.05 by one-way ANOVA followed by Tukey's test.

### Figure 4. DRK1 affects selected ABA-responsive marker transcripts.

(A) Relative expression of RD29B, RAB18, and ABI5 after 3 h ABA treatment in wild type, drk1-1, and complemented seedlings. Expression is normalized to mock-treated wild type. Values are means +/- SEM from three biological replicates. (B) Summary of how transcript data support broader ABA-response attenuation without proving guard-cell-specific transcriptional control.

### Figure 5. Evidence-bounded working model.

DRK1 contributes to the full ABA-induced stomatal closure response and is associated with ABA-triggered ROS accumulation and selected ABA-responsive transcript outputs. Dashed arrows indicate unresolved pathway placement.

## Supplementary Table 1. Statistical summary

| Assay | Comparison | Mean difference | P value | Interpretation |
|---|---|---:|---:|---|
| Stomatal aperture | WT ABA vs drk1-1 ABA | 1.53 um | <0.0001 | drk1-1 remains wider after ABA |
| Stomatal aperture | drk1-1 ABA vs complement ABA | 1.15 um | <0.0001 | complementation partially restores closure |
| ROS fluorescence | WT ABA vs drk1-1 ABA | 1.26-fold | 0.0007 | ABA-induced ROS is reduced in drk1-1 |
| qRT-PCR RD29B | WT ABA vs drk1-1 ABA | 3.2-fold | 0.0018 | marker induction is attenuated |
| qRT-PCR RAB18 | WT ABA vs drk1-1 ABA | 3.1-fold | 0.0021 | marker induction is attenuated |
| qRT-PCR ABI5 | WT ABA vs drk1-1 ABA | 1.3-fold | 0.0180 | marker induction is attenuated |

## Supplementary Table 2. Reproducibility checklist for the synthetic example

| Category | Reported Detail |
|---|---|
| Biological material | Arabidopsis Col-0, drk1-1 loss-of-function line, native-promoter DRK1 complementation line |
| Treatment | 10 uM ABA or matched solvent control; 2 h for stomatal assays, 20 min for ROS imaging, 3 h for qRT-PCR |
| Replicates | Three independent biological replicates; 60 stomata per genotype and treatment for aperture assays; three technical qPCR replicates |
| Controls | Mock treatment, wild-type baseline, mutant comparison, complementation line, no-template and no-reverse-transcription qPCR controls |
| Quantification | ImageJ aperture measurement and guard-cell fluorescence segmentation; 2^-Delta Delta Ct for qRT-PCR |
| Exclusion rules | Damaged leaves, edge stomata, out-of-focus images, saturated fluorescence images, and RNA samples outside purity thresholds |
| Statistics | Two-way ANOVA for stomatal aperture; one-way ANOVA for ABA-treated ROS and qRT-PCR comparisons; Tukey post hoc tests |

## References

1. Schroeder JI, Kwak JM, Allen GJ. Guard cell abscisic acid signalling and engineering drought hardiness in plants. Nature. 2001;410:327-330. doi:10.1038/35066500
2. Cutler SR, Rodriguez PL, Finkelstein RR, Abrams SR. Abscisic acid: emergence of a core signaling network. Annual Review of Plant Biology. 2010;61:651-679. doi:10.1146/annurev-arplant-042809-112122
3. Pei ZM, Murata Y, Benning G, Thomine S, Klusener B, Allen GJ, Grill E, Schroeder JI. Calcium channels activated by hydrogen peroxide mediate abscisic acid signalling in guard cells. Nature. 2000;406:731-734. doi:10.1038/35021067
4. Kwak JM, Mori IC, Pei ZM, Leonhardt N, Torres MA, Dangl JL, Bloom RE, Bodde S, Jones JDG, Schroeder JI. NADPH oxidase AtrbohD and AtrbohF genes function in ROS-dependent ABA signaling in Arabidopsis. EMBO Journal. 2003;22:2623-2633. doi:10.1093/emboj/cdg277
5. Park SY, Fung P, Nishimura N, Jensen DR, Fujii H, Zhao Y, Lumba S, Santiago J, Rodrigues A, Chow TF, et al. Abscisic acid inhibits type 2C protein phosphatases via the PYR/PYL family of START proteins. Science. 2009;324:1068-1071. doi:10.1126/science.1173041
6. Ma Y, Szostkiewicz I, Korte A, Moes D, Yang Y, Christmann A, Grill E. Regulators of PP2C phosphatase activity function as abscisic acid sensors. Science. 2009;324:1064-1068. doi:10.1126/science.1172408
7. Mustilli AC, Merlot S, Vavasseur A, Fenzi F, Giraudat J. Arabidopsis OST1 protein kinase mediates the regulation of stomatal aperture by abscisic acid and acts upstream of reactive oxygen species production. The Plant Cell. 2002;14:3089-3099. doi:10.1105/tpc.007906
8. Vahisalu T, Kollist H, Wang YF, Nishimura N, Chan WY, Valerio G, Lamminmaki A, Brosche M, Moldau H, Desikan R, et al. SLAC1 is required for plant guard cell S-type anion channel function in stomatal signalling. Nature. 2008;452:487-491. doi:10.1038/nature06608
9. Geiger D, Scherzer S, Mumm P, Stange A, Marten I, Bauer H, Ache P, Matschi S, Liese A, Al-Rasheid KAS, Romeis T, Hedrich R. Activity of guard cell anion channel SLAC1 is controlled by drought-stress signaling kinase-phosphatase pair. Proceedings of the National Academy of Sciences USA. 2009;106:21425-21430. doi:10.1073/pnas.0903532106
10. Brandt B, Munemasa S, Wang C, Nguyen D, Yong T, Yang PG, Poretsky E, Belknap TF, Waadt R, Aleman F, Schroeder JI. Calcium specificity signaling mechanisms in abscisic acid signal transduction in Arabidopsis guard cells. eLife. 2015;4:e03599. doi:10.7554/eLife.03599
