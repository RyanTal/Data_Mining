# UCSAS 2024 USOPC Data Challenge

This research utilizes data scraping, cleaning, and modeling, integrating machine learning models and combinatorial optimization algorithms to identify the optimal Men's and Women's Teams and Individual USA Olympic Artistic Gymnasts for the 2024 Olympic Games, defined as maximizing the total medal count. It adopts a novel approach with Metaheuristics Algorithms, including Randomized Heuristic, Tabu Search, and Variable Neighborhood Search, surpassing traditional mixed-integer linear programming. Grounded in meticulous data analysis, the study strategically positions Team USA to maximize their medal count in the Paris 2024 Olympics.

## Folder Structure

---

- [Data_Mining](.)

  - `README.md` - `README`
  - `Notes for Report.ipynb` - `Notes for Report`
  - `UCSAS 2024 USOPC Data Challenge.ipynb` - `UCSAS 2024 USOPC Data Challenge`
  - `Data Sources.ipynb` - `Data Sources`
  - `To Do and  Questions.ipynb` - `To Do and  Questions`

- [scraping](scraping)

  - [men](scraping/men)

    - `olympic winners.ipynb` - `olympic winners`

    - [eu19games_vt](scraping/men/eu19games_vt)

      - `eu19games_vt.py` - `eu19games_vt`
      - `european_games2019vt.csv` - `european_games2019vt`

    - [world_cup2019stuttgart](scraping/men/world_cup2019stuttgart)

      - `iaa.csv` - `iaa`
      - `wc19stutt.py` - `wc19stutt`

    - [olympics](scraping/men/olympics)

      - [mens202olympics_fianl](scraping/men/olympics/mens202olympics_fianl)

        - `Gymnastics_ 2020_Olympics_Men's_artistic_pommel_horse.csv` - `Gymnastics_ 2020_Olympics_Men's_artistic_pommel_horse`
        - `Gymnastics_ 2020_Olympics_Men's_artistic_vault.csv` - `Gymnastics_ 2020_Olympics_Men's_artistic_vault`
        - `men2020olympic_floor.py` - `men2020olympic_floor`
        - `men2020olympic_ring.py` - `men2020olympic_ring`
        - `Gymnastics_ 2020_Olympics_Men's_artistic_parallel_bars.csv` - `Gymnastics_ 2020_Olympics_Men's_artistic_parallel_bars`
        - `Gymnastics_ 2020_Olympics_Men's_artistic_team_all-around.csv` - `Gymnastics_ 2020_Olympics_Men's_artistic_team_all-around`
        - `men2020olympic_hb.py` - `men2020olympic_hb`
        - `men2020olympic_pb.py` - `men2020olympic_pb`
        - `Gymnastics_ 2020_Olympics_Men's_artistic_Individual_all-around.csv` - `Gymnastics_ 2020_Olympics_Men's_artistic_Individual_all-around`
        - `men2020olympic_team.py` - `men2020olympic_team`
        - `men2020olympic_ph.py` - `men2020olympic_ph`
        - `men2020olympic_vault.py` - `men2020olympic_vault`
        - `Gymnastics_ 2020_Olympics_Men's_artistic_floor.csv` - `Gymnastics_ 2020_Olympics_Men's_artistic_floor`
        - `men2020olympics_iaa.py` - `men2020olympics_iaa`
        - `Gymnastics_ 2020_Olympics_Men's_artistic_rings.csv` - `Gymnastics_ 2020_Olympics_Men's_artistic_rings`
        - `Gymnastics_ 2020_Olympics_Men's_artistic_horizontal_bar.csv` - `Gymnastics_ 2020_Olympics_Men's_artistic_horizontal_bar`

      - [olympic2016men](scraping/men/olympics/olympic2016men)
        - `Gymnastics_ 2016_Olympics_Men's_artistic_parallel_bars.csv` - `Gymnastics_ 2016_Olympics_Men's_artistic_parallel_bars`
        - `men2016olympic_rings.py` - `men2016olympic_rings`
        - `Gymnastics_ 2016_Olympics_Men's_artistic_vault.csv` - `Gymnastics_ 2016_Olympics_Men's_artistic_vault`
        - `Gymnastics_ 2016_Olympics_Men's_artistic_horizontal_bars.csv` - `Gymnastics_ 2016_Olympics_Men's_artistic_horizontal_bars`
        - `men2016olympic_team.py` - `men2016olympic_team`
        - `men2016olympic_vault.py` - `men2016olympic_vault`
        - `Gymnastics_ 2016_Olympics_Men's_artistic_pommel_horse.csv` - `Gymnastics_ 2016_Olympics_Men's_artistic_pommel_horse`
        - `Gymnastics_ 2016_Olympics_Men's_artistic_individual_all-around.csv` - `Gymnastics_ 2016_Olympics_Men's_artistic_individual_all-around`
        - `men2016olympic_hb.py` - `men2016olympic_hb`
        - `men2016olympic_pb.py` - `men2016olympic_pb`
        - `Gymnastics_ 2016_Olympics_Men's_artistic_team_all-around.csv` - `Gymnastics_ 2016_Olympics_Men's_artistic_team_all-around`
        - `men2016olympic_floor.py` - `men2016olympic_floor`
        - `men2016olympic_iaa.py` - `men2016olympic_iaa`
        - `men2016olympic_ph.py` - `men2016olympic_ph`
        - `Gymnastics_ 2016_Olympics_Men's_artistic_rings.csv` - `Gymnastics_ 2016_Olympics_Men's_artistic_rings`
        - `Gymnastics_ 2016_Olympics_Men's_artistic_floor.csv` - `Gymnastics_ 2016_Olympics_Men's_artistic_floor`

    - [world_championship2023](scraping/men/world_championship2023)

      - `table_2.csv` - `table_2`
      - `table_3.csv` - `table_3`
      - `table_1.csv` - `table_1`
      - `table_4.csv` - `table_4`
      - `table_5.csv` - `table_5`
      - `table_7.csv` - `table_7`
      - `table_6.csv` - `table_6`
      - `table_12.csv` - `table_12`
      - `iaa.csv` - `iaa`
      - `table_13.csv` - `table_13`
      - `table_11.csv` - `table_11`
      - `table_10.csv` - `table_10`
      - `table_9.csv` - `table_9`
      - `table_14.csv` - `table_14`
      - `table_15.csv` - `table_15`
      - `iaaq.csv` - `iaaq`
      - `world23champ.py` - `world23champ`

    - [world_championship2022](scraping/men/world_championship2022)

      - `table_2.csv` - `table_2`
      - `table_3.csv` - `table_3`
      - `table_1.csv` - `table_1`
      - `table_4.csv` - `table_4`
      - `table_5.csv` - `table_5`
      - `table_7.csv` - `table_7`
      - `table_6.csv` - `table_6`
      - `table_12.csv` - `table_12`
      - `iaa.csv` - `iaa`
      - `table_13.csv` - `table_13`
      - `table_11.csv` - `table_11`
      - `table_10.csv` - `table_10`
      - `table_9.csv` - `table_9`
      - `table_14.csv` - `table_14`
      - `table_15.csv` - `table_15`
      - `iaaq.csv` - `iaaq`
      - `world22champ.py` - `world22champ`

    - [world_cup2021Doha](scraping/men/world_cup2021Doha)

      - `hbq.csv` - `hbq`
      - `fxq.csv` - `fxq`
      - `phq.csv` - `phq`
      - `vt.csv` - `vt`
      - `pbq.csv` - `pbq`
      - `hb.csv` - `hb`
      - `fx.csv` - `fx`
      - `pb.csv` - `pb`
      - `vtq.csv` - `vtq`
      - `ph.csv` - `ph`
      - `sr.csv` - `sr`
      - `srq.csv` - `srq`
      - `wc2021doha.py` - `wc2021doha`

    - [winter_cup2022](scraping/men/winter_cup2022)

      - `winter22cup.py` - `winter22cup`
      - `table_2.csv` - `table_2`
      - `table_3.csv` - `table_3`
      - `table_1.csv` - `table_1`
      - `table_4.csv` - `table_4`
      - `table_5.csv` - `table_5`
      - `table_6.csv` - `table_6`
      - `iaa.csv` - `iaa`

    - [winter_cup2023](scraping/men/winter_cup2023)

      - `table_2.csv` - `table_2`
      - `table_3.csv` - `table_3`
      - `table_1.csv` - `table_1`
      - `table_4.csv` - `table_4`
      - `table_5.csv` - `table_5`
      - `table_7.csv` - `table_7`
      - `winter23cup.py` - `winter23cup`
      - `table_6.csv` - `table_6`
      - `table_12.csv` - `table_12`
      - `iaa.csv` - `iaa`
      - `table_13.csv` - `table_13`
      - `table_8.csv` - `table_8`
      - `table_11.csv` - `table_11`
      - `table_10.csv` - `table_10`
      - `table_9.csv` - `table_9`

    - [universiade2019](scraping/men/universiade2019)

      - `hbq.csv` - `hbq`
      - `fxq.csv` - `fxq`
      - `phq.csv` - `phq`
      - `vt.csv` - `vt`
      - `pbq.csv` - `pbq`
      - `hb.csv` - `hb`
      - `fx.csv` - `fx`
      - `pb.csv` - `pb`
      - `iaa.csv` - `iaa`
      - `ph.csv` - `ph`
      - `sr.csv` - `sr`
      - `srq.csv` - `srq`
      - `universiade2019.py` - `universiade2019`
      - `iaaq.csv` - `iaaq`

    - [world_championship2018](scraping/men/world_championship2018)

      - `world18champ_vt.py` - `world18champ_vt`
      - `world_championship2018sr.csv` - `world_championship2018sr`
      - `world_championship2018ph.csv` - `world_championship2018ph`
      - `world18champph.py` - `world18champph`
      - `world_championship2018iaa.csv` - `world_championship2018iaa`
      - `world8champ_iaa_qual.py` - `world8champ_iaa_qual`
      - `world18champ_pb.py` - `world18champ_pb`
      - `world18champs_pb_qual.py` - `world18champs_pb_qual`
      - `world18champ_hb.py` - `world18champ_hb`
      - `world_championship2018iaa_qual.csv` - `world_championship2018iaa_qual`
      - `world18champ_fx_qual.py` - `world18champ_fx_qual`
      - `world_championship2018vt.csv` - `world_championship2018vt`
      - `world18champ_fx.py` - `world18champ_fx`
      - `world_championship2018ph_qual.csv` - `world_championship2018ph_qual`
      - `world18champ_ph_qual.py` - `world18champ_ph_qual`
      - `world18champ_sr_qual.py` - `world18champ_sr_qual`
      - `world_championship2018hb_qual.csv` - `world_championship2018hb_qual`
      - `world_championship2018pb_qual.csv` - `world_championship2018pb_qual`
      - `world_championship2018hb.csv` - `world_championship2018hb`
      - `world18champ_hb_qual.py` - `world18champ_hb_qual`
      - `world_championship2018sr_qual.csv` - `world_championship2018sr_qual`
      - `world18champ_sr.py` - `world18champ_sr`
      - `world_championship2018fx_qual.csv` - `world_championship2018fx_qual`
      - `world_championship2018pb.csv` - `world_championship2018pb`
      - `world_championship2018fx.csv` - `world_championship2018fx`
      - `world18champ_iaa.py` - `world18champ_iaa`

    - [world_championship2021](scraping/men/world_championship2021)

      - `hbq.csv` - `hbq`
      - `fxq.csv` - `fxq`
      - `phq.csv` - `phq`
      - `vt.csv` - `vt`
      - `pbq.csv` - `pbq`
      - `hb.csv` - `hb`
      - `fx.csv` - `fx`
      - `pb.csv` - `pb`
      - `iaa.csv` - `iaa`
      - `vtq.csv` - `vtq`
      - `ph.csv` - `ph`
      - `sr.csv` - `sr`
      - `srq.csv` - `srq`
      - `world21champs.py` - `world21champs`
      - `iaaq.csv` - `iaaq`

    - [winter_cup2020](scraping/men/winter_cup2020)

      - `vt.csv` - `vt`
      - `hb.csv` - `hb`
      - `fx.csv` - `fx`
      - `pb.csv` - `pb`
      - `wc2020melb.py` - `wc2020melb`
      - `iaa.csv` - `iaa`
      - `ph.csv` - `ph`
      - `sr.csv` - `sr`
      - `wint20cup.py` - `wint20cup`

    - [world_champis2019](scraping/men/world_champis2019)

      - `hbq.csv` - `hbq`
      - `fxq.csv` - `fxq`
      - `phq.csv` - `phq`
      - `vt.csv` - `vt`
      - `wc2019.py` - `wc2019`
      - `pbq.csv` - `pbq`
      - `hb.csv` - `hb`
      - `world19scrape.py` - `world19scrape`
      - `fx.csv` - `fx`
      - `pb.csv` - `pb`
      - `table_12.csv` - `table_12`
      - `iaa.csv` - `iaa`
      - `ph.csv` - `ph`
      - `sr.csv` - `sr`
      - `srq.csv` - `srq`
      - `iaaq.csv` - `iaaq`

    - [world_cup2019tokyo](scraping/men/world_cup2019tokyo)

      - `wc2019tokyo.py` - `wc2019tokyo`
      - `iaa.csv` - `iaa`

    - [men23top](scraping/men/men23top)

      - `phd.csv` - `phd`
      - `fxd.csv` - `fxd`
      - `hbd.csv` - `hbd`
      - `vt_combo_d.csv` - `vt_combo_d`
      - `vt_single.csv` - `vt_single`
      - `pbd.csv` - `pbd`
      - `hb.csv` - `hb`
      - `fx.csv` - `fx`
      - `pb.csv` - `pb`
      - `men23top.py` - `men23top`
      - `iaa.csv` - `iaa`
      - `ph.csv` - `ph`
      - `sr.csv` - `sr`
      - `srd.csv` - `srd`
      - `vt_avg.csv` - `vt_avg`

    - [world_cup2019melbourne](scraping/men/world_cup2019melbourne)

      - `world_cup_melbourne2019vt.csv` - `world_cup_melbourne2019vt`
      - `wc19melb_pb.py` - `wc19melb_pb`
      - `wc19melb_pb_qual.py` - `wc19melb_pb_qual`
      - `wc19melb_fx_qual.py` - `wc19melb_fx_qual`
      - `wc19melb_ph.py` - `wc19melb_ph`
      - `wc19melb_hb_qual.py` - `wc19melb_hb_qual`
      - `wc19melb_ph_qual.py` - `wc19melb_ph_qual`
      - `wc19melb_sr_qual.py` - `wc19melb_sr_qual`
      - `world_cup_melbourne2019fx.csv` - `world_cup_melbourne2019fx`
      - `world_cup_melbourne2019pb.csv` - `world_cup_melbourne2019pb`
      - `wc19melb_vt.py` - `wc19melb_vt`
      - `world_cup_melbourne2019hb.csv` - `world_cup_melbourne2019hb`
      - `world_cup_melbourne2019sr.csv` - `world_cup_melbourne2019sr`
      - `wc19melb_sr.py` - `wc19melb_sr`
      - `world_cup_melbourne2019ph.csv` - `world_cup_melbourne2019ph`
      - `world_cup_melbourne2019pb_qual.csv` - `world_cup_melbourne2019pb_qual`
      - `world_cup_melbourne2019hb_qual.csv` - `world_cup_melbourne2019hb_qual`
      - `wc19melb_fx.py` - `wc19melb_fx`
      - `world_cup_melbourne2019ph_qual.csv` - `world_cup_melbourne2019ph_qual`
      - `world_cup_melbourne2019fx_qual.csv` - `world_cup_melbourne2019fx_qual`
      - `wc19melb_hb.py` - `wc19melb_hb`
      - `world_cup_melbourne2019sr_qual.csv` - `world_cup_melbourne2019sr_qual`

    - [world_cup2020baku](scraping/men/world_cup2020baku)

      - `world2020cup_baku_vt.py` - `world2020cup_baku_vt`
      - `wc20baku_fx_qual.py` - `wc20baku_fx_qual`
      - `wc20baku_pb_qual.py` - `wc20baku_pb_qual`
      - `world_cup_baku2020fx_qual.csv` - `world_cup_baku2020fx_qual`
      - `world_cup_baku2020vt.csv` - `world_cup_baku2020vt`
      - `world_cup_baku2020sr_qual.csv` - `world_cup_baku2020sr_qual`
      - `wc20baku_ph_qual.py` - `wc20baku_ph_qual`
      - `world_cup_baku2020pb_qual.csv` - `world_cup_baku2020pb_qual`
      - `wc20baku_sr_qual.py` - `wc20baku_sr_qual`
      - `world_cup_baku2020hb_qual.csv` - `world_cup_baku2020hb_qual`
      - `wc20baku_hb_qual.py` - `wc20baku_hb_qual`
      - `world_cup_baku2020ph_qual.csv` - `world_cup_baku2020ph_qual`

    - [world_cup2019birmingham](scraping/men/world_cup2019birmingham)
      - `iaa.csv` - `iaa`
      - `wc19birm.py` - `wc19birm`

  - [women](scraping/women)

    - [wc17w](scraping/women/wc17w)

      - `wc17w_bb.csv` - `wc17w_bb`
      - `wc17w_bb.py` - `wc17w_bb`
      - `wc17w_ub.py` - `wc17w_ub`
      - `wc17w_vt.csv` - `wc17w_vt`
      - `wc17w_iaa.csv` - `wc17w_iaa`
      - `wc17w_vt.py` - `wc17w_vt`
      - `wc17w_fx.csv` - `wc17w_fx`
      - `wc17w_iaa.py` - `wc17w_iaa`
      - `wc17w_ub.csv` - `wc17w_ub`
      - `wc17w_fx.py` - `wc17w_fx`

    - [wc14w](scraping/women/wc14w)

      - `wc14w_fx.csv` - `wc14w_fx`
      - `wc14w_fx.py` - `wc14w_fx`
      - `wc14w_bb.csv` - `wc14w_bb`
      - `wc14w_vt.csv` - `wc14w_vt`
      - `wc14w_iaa.csv` - `wc14w_iaa`
      - `wc14w_ub.csv` - `wc14w_ub`
      - `wc14w_ub.py` - `wc14w_ub`
      - `wc14w_bb.py` - `wc14w_bb`
      - `wc14w_vt.py` - `wc14w_vt`
      - `wc14w_iaa.py` - `wc14w_iaa`

    - [worldcup13cott](scraping/women/worldcup13cott)

      - `worldcup2013cott_ub_qual.csv` - `worldcup2013cott_ub_qual`
      - `wc13cott_vt.py` - `wc13cott_vt`
      - `wc13cott_bb.py` - `wc13cott_bb`
      - `wc13cott_ub.py` - `wc13cott_ub`
      - `worldcup2013cott_ub.csv` - `worldcup2013cott_ub`
      - `wc13cott_fx.py` - `wc13cott_fx`
      - `wc13cott_fx_qual.py` - `wc13cott_fx_qual`
      - `worldcup2013cott_vt.csv` - `worldcup2013cott_vt`
      - `worldcup2013cott_bb_qual.csv` - `worldcup2013cott_bb_qual`
      - `wc13cott_ub.qual.py` - `wc13cott_ub.qual`
      - `worldcup2013cott_bb.csv` - `worldcup2013cott_bb`
      - `worldcup2013cott_fx.csv` - `worldcup2013cott_fx`
      - `worldcup2013cott_fx_qual.csv` - `worldcup2013cott_fx_qual`
      - `wc13cott_bb_qual.py` - `wc13cott_bb_qual`

    - [olympics](scraping/women/olympics)

      - [womens2020olympics](scraping/women/olympics/womens2020olympics)

        - `women2020olympic_team.py` - `women2020olympic_team`
        - `women2020ub.py` - `women2020ub`
        - `women2020bb.py` - `women2020bb`
        - `Gymnastics_ 2020_Olympics_women's_artistic_floor.csv` - `Gymnastics_ 2020_Olympics_women's_artistic_floor`
        - `Gymnastics_ 2020_Olympics_women's_artistic_team_all-around.csv` - `Gymnastics_ 2020_Olympics_women's_artistic_team_all-around`
        - `women2020iaa.py` - `women2020iaa`
        - `women2020vt.py` - `women2020vt`
        - `Gymnastics_ 2020_Olympics_women's_artistic_uneven_bars.csv` - `Gymnastics_ 2020_Olympics_women's_artistic_uneven_bars`
        - `Gymnastics_ 2020_Olympics_women's_artistic_individual_all-around.csv` - `Gymnastics_ 2020_Olympics_women's_artistic_individual_all-around`
        - `Gymnastics_ 2020_Olympics_women's_artistic_balance_beam.csv` - `Gymnastics_ 2020_Olympics_women's_artistic_balance_beam`
        - `women2020fx.py` - `women2020fx`
        - `Gymnastics_ 2020_Olympics_women's_artistic_vault.csv` - `Gymnastics_ 2020_Olympics_women's_artistic_vault`

      - [women2016olympics](scraping/women/olympics/women2016olympics)
        - `Gymnastics_ 2016_Olympics_women's_artistic_team_all_around.csv` - `Gymnastics_ 2016_Olympics_women's_artistic_team_all_around`
        - `women2016bb.py` - `women2016bb`
        - `women2016ub.py` - `women2016ub`
        - `Gymnastics_ 2016_Olympics_women's_artistic_balance_beam.csv` - `Gymnastics_ 2016_Olympics_women's_artistic_balance_beam`
        - `delete this .ipynb` - `delete this `
        - `Gymnastics_ 2016_Olympics_women's_artistic_vault.csv` - `Gymnastics_ 2016_Olympics_women's_artistic_vault`
        - `Gymnastics_ 2016_Olympics_women's_artistic_individual_all_around.csv` - `Gymnastics_ 2016_Olympics_women's_artistic_individual_all_around`
        - `women2016vt.py` - `women2016vt`
        - `Gymnastics_ 2016_Olympics_women's_artistic_uneven_bar.csv` - `Gymnastics_ 2016_Olympics_women's_artistic_uneven_bar`
        - `Gymnastics_ 2016_Olympics_women's_artistic_floor.csv` - `Gymnastics_ 2016_Olympics_women's_artistic_floor`
        - `women2016.py` - `women2016`
        - `women2016fx.py` - `women2016fx`
        - `women2016iaa.py` - `women2016iaa`

    - [jesolo15](scraping/women/jesolo15)

      - `jesolo15vt.py` - `jesolo15vt`
      - `jesolo2015ub.csv` - `jesolo2015ub`
      - `jesolo15ub.py` - `jesolo15ub`
      - `jesolo15bb.py` - `jesolo15bb`
      - `jesolo2015fx.csv` - `jesolo2015fx`
      - `jesolo15fx.py` - `jesolo15fx`
      - `jesolo2015bb.csv` - `jesolo2015bb`
      - `jesolo2015vt.csv` - `jesolo2015vt`

    - [euro21w](scraping/women/euro21w)

      - `euro21w_vt.py` - `euro21w_vt`
      - `euro21w.py` - `euro21w`
      - `euro21w_ub.csv` - `euro21w_ub`
      - `euro21w_ub.py` - `euro21w_ub`
      - `euro21w_bb.py` - `euro21w_bb`
      - `euro21w_fx.py` - `euro21w_fx`
      - `euro21w_fx.csv` - `euro21w_fx`
      - `euro21w_iaa.csv` - `euro21w_iaa`
      - `euro21w_bb.csv` - `euro21w_bb`
      - `euro21w_vt.csv` - `euro21w_vt`

    - [pan_america14](scraping/women/pan_america14)

      - `pan_american2014_vt.csv` - `pan_american2014_vt`
      - `pan_america14vt.py` - `pan_america14vt`
      - `pan_american2014_bb.csv` - `pan_american2014_bb`
      - `pan_american2014_fx.csv` - `pan_american2014_fx`
      - `pan_america14ub.py` - `pan_america14ub`
      - `pan_america14bb.py` - `pan_america14bb`
      - `pan_america14fx.py` - `pan_america14fx`
      - `pan_american2014_ub.csv` - `pan_american2014_ub`

    - [pan_america](scraping/women/pan_america)

      - `pa21w.csv` - `pa21w`
      - `pa21w_iaa.py` - `pa21w_iaa`

    - [iaa22_23](scraping/women/iaa22_23)

      - `chinese22championship_iaa.csv` - `chinese22championship_iaa`
      - `wint_cup22iaa.py` - `wint_cup22iaa`
      - `china22champ.py` - `china22champ`
      - `world22champ_iaa.py` - `world22champ_iaa`
      - `winter_cup23iaa.csv` - `winter_cup23iaa`
      - `iaaq23.csv` - `iaaq23`
      - `south_america22champ.py` - `south_america22champ`
      - `us22champ.py` - `us22champ`
      - `iaaq22.csv` - `iaaq22`
      - `south_america22championship_iaa.csv` - `south_america22championship_iaa`
      - `wint23cup_iaa.py` - `wint23cup_iaa`
      - `wint22cup_iaa.csv` - `wint22cup_iaa`
      - `usa22championship_iaa.csv` - `usa22championship_iaa`
      - `world23champ_iaa.py` - `world23champ_iaa`
      - `european22championship_iaa.csv` - `european22championship_iaa`
      - `european22championship.py` - `european22championship`
      - `iaa23.csv` - `iaa23`
      - `iaa22.csv` - `iaa22`

    - [british_championship15](scraping/women/british_championship15)

      - `british_championship2015vt.csv` - `british_championship2015vt`
      - `bc15vt.py` - `bc15vt`
      - `british_championship2015bb.csv` - `british_championship2015bb`
      - `british_championship2015fx.csv` - `british_championship2015fx`
      - `bc15ub.py` - `bc15ub`
      - `bc15bb.py` - `bc15bb`
      - `bc15fx.py` - `bc15fx`
      - `british_championship2015ub.csv` - `british_championship2015ub`

    - [miscellaneous](scraping/women/miscellaneous)

      - `Women2019_World_Artistic_Gymnastics_Championships.csv` - `Women2019_World_Artistic_Gymnastics_Championships`
      - `worldchamp15.py` - `worldchamp15`
      - `Women2011olympics.csv` - `Women2011olympics`
      - `Women2020olympics.csv` - `Women2020olympics`
      - `olymp16.py` - `olymp16`
      - `scrape2020_w_ind_allrnd.py` - `scrape2020_w_ind_allrnd`
      - `worldchamp18.py` - `worldchamp18`
      - `olymp20.py` - `olymp20`
      - `worldchamp19.py` - `worldchamp19`
      - `scrape2020_w_ind_floor.py` - `scrape2020_w_ind_floor`
      - `Women2015World_Artistic_Gymnastics_Championships.csv` - `Women2015World_Artistic_Gymnastics_Championships`
      - `Women2018_World_Artistic_Gymnastics_Championships.csv` - `Women2018_World_Artistic_Gymnastics_Championships`
      - `scrapewiki.py` - `scrapewiki`
      - `scraped_data.csv` - `scraped_data`
      - `Women2016olympics.csv` - `Women2016olympics`
      - `scrape2020.py` - `scrape2020`
      - `scrape2020qual_team.csv` - `scrape2020qual_team`
      - `scrape.py` - `scrape`
      - `individ_qual_2020.csv` - `individ_qual_2020`

    - [worldcup19doha](scraping/women/worldcup19doha)

      - `worldcup2019doha_qual_ub.csv` - `worldcup2019doha_qual_ub`
      - `worldcup2019doha_vt.csv` - `worldcup2019doha_vt`
      - `worldcup2019doha_bb.csv` - `worldcup2019doha_bb`
      - `worldcup19doha_fx.py` - `worldcup19doha_fx`
      - `worldcup2019doha_fx.csv` - `worldcup2019doha_fx`
      - `worldcup19doha_qual_fx.py` - `worldcup19doha_qual_fx`
      - `worldcup19doha-ub.py` - `worldcup19doha-ub`
      - `worldcup19doha_qual_ub.py` - `worldcup19doha_qual_ub`
      - `worldcup19doha_qual_bb.py` - `worldcup19doha_qual_bb`
      - `worldcup19doha_vt.py` - `worldcup19doha_vt`
      - `worldcup2019doha_qual_fx.csv` - `worldcup2019doha_qual_fx`
      - `worldcup2019doha_qual_bb.csv` - `worldcup2019doha_qual_bb`
      - `worldcup19doha_bb.py` - `worldcup19doha_bb`
      - `worldcup2019doha_ub.csv` - `worldcup2019doha_ub`

    - [wc19w](scraping/women/wc19w)

      - `wc19w_team.py` - `wc19w_team`
      - `wc19w_iaa.py` - `wc19w_iaa`
      - `wc19w_bb.py` - `wc19w_bb`
      - `wc19w_ub.py` - `wc19w_ub`
      - `wc19w_ub.csv` - `wc19w_ub`
      - `wc19w_vt.py` - `wc19w_vt`
      - `wc19w_bb.csv` - `wc19w_bb`
      - `wc19w_vt.csv` - `wc19w_vt`
      - `wc19w_team.csv` - `wc19w_team`
      - `wc19w_fx.py` - `wc19w_fx`
      - `wc19w_fx.csv` - `wc19w_fx`
      - `wc19w_iaa.csv` - `wc19w_iaa`

    - [worldcup14doha](scraping/women/worldcup14doha)

      - `worldcup2014doha_vt.csv` - `worldcup2014doha_vt`
      - `worldcup2014doha_bb_qual.csv` - `worldcup2014doha_bb_qual`
      - `wc14doha_fx.py` - `wc14doha_fx`
      - `wc14doha_fx_qual.py` - `wc14doha_fx_qual`
      - `worldcup2014doha_bb.csv` - `worldcup2014doha_bb`
      - `worldcup2014doha_fx_qual.csv` - `worldcup2014doha_fx_qual`
      - `worldcup2014doha_fx.csv` - `worldcup2014doha_fx`
      - `wc14doha_bb_qual.py` - `wc14doha_bb_qual`
      - `worldcup2014doha_ub_qual.csv` - `worldcup2014doha_ub_qual`
      - `wc14doha_vt.py` - `wc14doha_vt`
      - `wc14doha_bb.py` - `wc14doha_bb`
      - `wc14doha_ub.py` - `wc14doha_ub`
      - `worldcup2014doha_ub.csv` - `worldcup2014doha_ub`
      - `wc14doha_ub_qual.py` - `wc14doha_ub_qual`

    - [eurochamp2018](scraping/women/eurochamp2018)

      - `euro2018champ_bb_qual.csv` - `euro2018champ_bb_qual`
      - `euro18champ_vt.py` - `euro18champ_vt`
      - `euro2018champ_fx.csv` - `euro2018champ_fx`
      - `euro2018champ_bb.csv` - `euro2018champ_bb`
      - `euro18champ_ub_qual.py` - `euro18champ_ub_qual`
      - `euro2018champ_fx_qual.csv` - `euro2018champ_fx_qual`
      - `euro18champ_bb.py` - `euro18champ_bb`
      - `euro18champ_ub.py` - `euro18champ_ub`
      - `euro2018champ_vt.csv` - `euro2018champ_vt`
      - `euro2018champ_ub.csv` - `euro2018champ_ub`
      - `euro2018champ_ub_qual.csv` - `euro2018champ_ub_qual`
      - `euro18champ_fx.py` - `euro18champ_fx`
      - `euro18champ_fx_qual.py` - `euro18champ_fx_qual`
      - `euro18champ_bb_qual.py` - `euro18champ_bb_qual`

    - [eurochamp2021](scraping/women/eurochamp2021)

      - `euro21champ_fx_qual.py` - `euro21champ_fx_qual`
      - `euro21champ_bb_qual.py` - `euro21champ_bb_qual`
      - `euro21champ_fx.py` - `euro21champ_fx`
      - `euro2021champ_ub.csv` - `euro2021champ_ub`
      - `euro2021champ_ub_qual.csv` - `euro2021champ_ub_qual`
      - `euro2021champ_bb.csv` - `euro2021champ_bb`
      - `euro2021champ_vt.csv` - `euro2021champ_vt`
      - `euro2021champ_fx_qual.csv` - `euro2021champ_fx_qual`
      - `euro21champ_bb.py` - `euro21champ_bb`
      - `euro21champ_ub.py` - `euro21champ_ub`
      - `euro21champ_ub_qual.py` - `euro21champ_ub_qual`
      - `euro21champ_vt.py` - `euro21champ_vt`
      - `euro2021champ_bb_qual.csv` - `euro2021champ_bb_qual`
      - `euro2021champ_fx.csv` - `euro2021champ_fx`

    - [pacific_rim_championship16](scraping/women/pacific_rim_championship16)

      - `prc16ub.py` - `prc16ub`
      - `prc16bb.py` - `prc16bb`
      - `pac_rim_championshiop2016fx.csv` - `pac_rim_championshiop2016fx`
      - `pac_rim_championshiop2016vt.csv` - `pac_rim_championshiop2016vt`
      - `prc16vt.py` - `prc16vt`
      - `pac_rim_championshiop2016bb.csv` - `pac_rim_championshiop2016bb`
      - `pac_rim_championshiop2016ub.csv` - `pac_rim_championshiop2016ub`
      - `prc16fx.py` - `prc16fx`

    - [top2019scores](scraping/women/top2019scores)

      - `bb.csv` - `bb`
      - `vault_avg.csv` - `vault_avg`
      - `fx.csv` - `fx`
      - `topscores2020.py` - `topscores2020`
      - `vault.csv` - `vault`
      - `iaa.csv` - `iaa`
      - `uneven_bars.csv` - `uneven_bars`

    - [worldcup20Baku](scraping/women/worldcup20Baku)

      - `worldcup2020Baku_fx.csv` - `worldcup2020Baku_fx`
      - `worldcup2020Baku_fx.py` - `worldcup2020Baku_fx`
      - `worldcup2020Baku_vt.csv` - `worldcup2020Baku_vt`
      - `worldcup2020Baku_bb.csv` - `worldcup2020Baku_bb`
      - `worldcup2020Baku_bb.py` - `worldcup2020Baku_bb`
      - `worldcup2020Baku_ub.py` - `worldcup2020Baku_ub`
      - `worldcup2020Baku_ub.csv` - `worldcup2020Baku_ub`
      - `worldcup2020Baku_vt.py` - `worldcup2020Baku_vt`

    - [euro_games2019](scraping/women/euro_games2019)

      - `european_games2019_bb.csv` - `european_games2019_bb`
      - `european_games2019_fx_qual.csv` - `european_games2019_fx_qual`
      - `euro19games_ub_qual.py` - `euro19games_ub_qual`
      - `euro19games_ub.py` - `euro19games_ub`
      - `euro19games_bb.py` - `euro19games_bb`
      - `european_games2019_vt.csv` - `european_games2019_vt`
      - `european_games2019_bb_qual.csv` - `european_games2019_bb_qual`
      - `european_games2019_fx.csv` - `european_games2019_fx`
      - `euro19games_vt.py` - `euro19games_vt`
      - `euro19games_bb_qual.py` - `euro19games_bb_qual`
      - `european_games2019_ub_qual.csv` - `european_games2019_ub_qual`
      - `european_games2019_ub.csv` - `european_games2019_ub`
      - `euro19games_fx.py` - `euro19games_fx`
      - `euro19games_fx_qual.py` - `euro19games_fx_qual`

    - [top2020scores](scraping/women/top2020scores)

      - `bb.csv` - `bb`
      - `vt.csv` - `vt`
      - `top_scores2020.py` - `top_scores2020`
      - `fx.csv` - `fx`
      - `iaa.csv` - `iaa`
      - `vt_avg.csv` - `vt_avg`
      - `ub.csv` - `ub`

    - [universidad2019](scraping/women/universidad2019)

      - `uni19bb.csv` - `uni19bb`
      - `uni19vt.py` - `uni19vt`
      - `uni19vt.csv` - `uni19vt`
      - `uni19fx.csv` - `uni19fx`
      - `uni19ub.py` - `uni19ub`
      - `uni19bb.py` - `uni19bb`
      - `uni19fx.py` - `uni19fx`
      - `uni19ub.csv` - `uni19ub`

    - [wc_18w](scraping/women/wc_18w)

      - `wc18w_team.py` - `wc18w_team`
      - `wc18w_iaa.py` - `wc18w_iaa`
      - `wc18w_fx.py` - `wc18w_fx`
      - `wc18w_ub.csv` - `wc18w_ub`
      - `wc18w_vt.csv` - `wc18w_vt`
      - `wc18w_bb.csv` - `wc18w_bb`
      - `wc18w_bb.py` - `wc18w_bb`
      - `wc18w_ub.py` - `wc18w_ub`
      - `wc18w_fx.csv` - `wc18w_fx`
      - `wc18w_vt.py` - `wc18w_vt`
      - `wc18w_iaa.csv` - `wc18w_iaa`
      - `wc18w_team.csv` - `wc18w_team`

    - [qual2016](scraping/women/qual2016)

      - `scrape2016qual_team.py` - `scrape2016qual_team`
      - `scrape2016_team_qual.csv` - `scrape2016_team_qual`

    - [iaa_w](scraping/women/iaa_w)

      - `wc19iaa.py` - `wc19iaa`
      - `women_top_iaa.py` - `women_top_iaa`
      - `wc19tokyo_iaa.py` - `wc19tokyo_iaa`
      - `wc18birm_iaa.py` - `wc18birm_iaa`
      - `worldcup_tokyo2019_iaa.csv` - `worldcup_tokyo2019_iaa`
      - `worldcup_birmingham2018_iaa.csv` - `worldcup_birmingham2018_iaa`
      - `top_women_iaa.csv` - `top_women_iaa`
      - `iaaq19.csv` - `iaaq19`
      - `wc18stutt_iaa.py` - `wc18stutt_iaa`
      - `worldcup_stuttgart2019_iaa.csv` - `worldcup_stuttgart2019_iaa`
      - `wc18iaa.csv` - `wc18iaa`
      - `worldcup_birmingham2019_iaa.csv` - `worldcup_birmingham2019_iaa`
      - `world18champs_18.py` - `world18champs_18`
      - `wc18tokyo_iaa.py` - `wc18tokyo_iaa`
      - `worldcup_2018tokyo_iaa.csv` - `worldcup_2018tokyo_iaa`
      - `worldcup2018_iaa.csv` - `worldcup2018_iaa`
      - `iaaq.csv` - `iaaq`
      - `wc19stutt_iaa.py` - `wc19stutt_iaa`
      - `iaa19.csv` - `iaa19`
      - `wc19birm_iaa.py` - `wc19birm_iaa`

    - [final2020](scraping/women/final2020)

      - `scrape2020final_indv_bb.csv` - `scrape2020final_indv_bb`
      - `scrape2020final_team_allrnd.csv` - `scrape2020final_team_allrnd`
      - `scrape2020final_indiv_floor.csv` - `scrape2020final_indiv_floor`
      - `scrape2020final_team_allrnd.py` - `scrape2020final_team_allrnd`
      - `scrape2020final_indiv_allrnd.csv` - `scrape2020final_indiv_allrnd`
      - `final2020indv_bb.py` - `final2020indv_bb`
      - `final2020indv_uneven.py` - `final2020indv_uneven`
      - `scrape2020+_w_vault_final.py` - `scrape2020+_w_vault_final`
      - `scrape2020final_indiv_vault.csv` - `scrape2020final_indiv_vault`
      - `scrape2020final_indv_uneven.csv` - `scrape2020final_indv_uneven`

    - [worldcup19melbourne](scraping/women/worldcup19melbourne)

      - `worldcup2019melbourne_bb.csv` - `worldcup2019melbourne_bb`
      - `worldcup2019melbourne_bb_qual.csv` - `worldcup2019melbourne_bb_qual`
      - `worldcup2019melbourne_vt.csv` - `worldcup2019melbourne_vt`
      - `wc19melb_fx_qual.py` - `wc19melb_fx_qual`
      - `wc19melb_bb.py` - `wc19melb_bb`
      - `wc19melb_ub.py` - `wc19melb_ub`
      - `wc19melb_bb_qual.py` - `wc19melb_bb_qual`
      - `worldcup2019melbourne_fx_qual.csv` - `worldcup2019melbourne_fx_qual`
      - `wc19melb_vt.py` - `wc19melb_vt`
      - `worldcup2019melbourne_fx.csv` - `worldcup2019melbourne_fx`
      - `worldcup2019melbourne_ub_qual.csv` - `worldcup2019melbourne_ub_qual`
      - `wc19melb_ub_qual.py` - `wc19melb_ub_qual`
      - `worldcup2019melbourne_ub.csv` - `worldcup2019melbourne_ub`
      - `worldcup2020melb_vt.py` - `worldcup2020melb_vt`
      - `wc19melb_fx.py` - `wc19melb_fx`

    - [worldcup15cottbus](scraping/women/worldcup15cottbus)

      - `worldcup15cott_ub_qual.py` - `worldcup15cott_ub_qual`
      - `worldcup2015cott_qual_ub.csv` - `worldcup2015cott_qual_ub`
      - `worldcup2015cott_fx.csv` - `worldcup2015cott_fx`
      - `worldcup15cottbus_vt.py` - `worldcup15cottbus_vt`
      - `worldcup2015cott_vt.csv` - `worldcup2015cott_vt`
      - `worldcup15cott_qual_bb.py` - `worldcup15cott_qual_bb`
      - `worldcup15cott_bb.py` - `worldcup15cott_bb`
      - `worldcup15cott_ub.py` - `worldcup15cott_ub`
      - `worldcup2015cott_bb.csv` - `worldcup2015cott_bb`
      - `worldcup15cott_fx.py` - `worldcup15cott_fx`
      - `worldcup2015cott_ub.csv` - `worldcup2015cott_ub`
      - `worldcup15cott_qual_fx.py` - `worldcup15cott_qual_fx`
      - `worldcup2015cott_qual_fx.csv` - `worldcup2015cott_qual_fx`
      - `worldcup2015cott_qual_bb.csv` - `worldcup2015cott_qual_bb`

    - [worldcup18jesolo](scraping/women/worldcup18jesolo)

      - `wc18jesolo_ub.py` - `wc18jesolo_ub`
      - `wc18jesolo_bb.py` - `wc18jesolo_bb`
      - `worldcup2018jesolo_ub.csv` - `worldcup2018jesolo_ub`
      - `wc18jesolo_vt.py` - `wc18jesolo_vt`
      - `worldcup2018jesolo_bb.csv` - `worldcup2018jesolo_bb`
      - `worldcup2018jesolo_vt.csv` - `worldcup2018jesolo_vt`
      - `wc18jesolo_fx.py` - `wc18jesolo_fx`
      - `worldcup2018jesolo_fx.csv` - `worldcup2018jesolo_fx`

    - [wc15w](scraping/women/wc15w)

      - `wc15w_fx.csv` - `wc15w_fx`
      - `wc15w_ub.py` - `wc15w_ub`
      - `wc15w_bb.py` - `wc15w_bb`
      - `wc15w_vt.csv` - `wc15w_vt`
      - `wc15w_bb.csv` - `wc15w_bb`
      - `wc15w_vt.py` - `wc15w_vt`
      - `wc15w_iaa.csv` - `wc15w_iaa`
      - `wc15w_ub.csv` - `wc15w_ub`
      - `wc15w_fx.py` - `wc15w_fx`
      - `wc15w_iaa.py` - `wc15w_iaa`

    - [european_championship2015](scraping/women/european_championship2015)

      - `euro15champ_bb_qual.py` - `euro15champ_bb_qual`
      - `euro15champ_vt.py` - `euro15champ_vt`
      - `european_championship2015fx.csv` - `european_championship2015fx`
      - `european_championship2015fx_qual.csv` - `european_championship2015fx_qual`
      - `euro15champ_bb.py` - `euro15champ_bb`
      - `euro15champ_ub.py` - `euro15champ_ub`
      - `european_championship2015bb_qual.csv` - `european_championship2015bb_qual`
      - `european_championship2015vt.csv` - `european_championship2015vt`
      - `european_championship2015bb.csv` - `european_championship2015bb`
      - `euro15champ_fx_qual.py` - `euro15champ_fx_qual`
      - `euro15champ_ub_qual.py` - `euro15champ_ub_qual`
      - `euro15champ_fx.py` - `euro15champ_fx`
      - `european_championship2015ub.csv` - `european_championship2015ub`
      - `european_championship2015ub_qual.csv` - `european_championship2015ub_qual`

    - [gymternet](scraping/women/gymternet)

      - `gymternet_scrape.py` - `gymternet_scrape`
      - `team2023camp.csv` - `team2023camp`
      - `best_vault2023.csv` - `best_vault2023`
      - `team2023camp.py` - `team2023camp`
      - `best_UB2023.csv` - `best_UB2023`
      - `gymternet .ipynb` - `gymternet `
      - `best_scores2023.csv` - `best_scores2023`
      - `best_ub2023.py` - `best_ub2023`
      - `best_bb2023.py` - `best_bb2023`
      - `best_BB2023.csv` - `best_BB2023`
      - `best_vault2023.py` - `best_vault2023`
      - `best_floor2023.py` - `best_floor2023`
      - `best_floor2023.csv` - `best_floor2023`

    - [universiade2015](scraping/women/universiade2015)

      - `uni15fx_qual.py` - `uni15fx_qual`
      - `universiade2015fx_qual.csv` - `universiade2015fx_qual`
      - `uni15vt.py` - `uni15vt`
      - `universiade2015bb_qual.csv` - `universiade2015bb_qual`
      - `universiade2015ub.csv` - `universiade2015ub`
      - `uni15bb_qual.py` - `uni15bb_qual`
      - `uni15ub.py` - `uni15ub`
      - `uni15bb.py` - `uni15bb`
      - `universiade2015vt.csv` - `universiade2015vt`
      - `uni15fx.py` - `uni15fx`
      - `universiade2015bb.csv` - `universiade2015bb`
      - `universiade2015fx.csv` - `universiade2015fx`
      - `universiade2015ub_qual.csv` - `universiade2015ub_qual`
      - `uni15ub_qual.py` - `uni15ub_qual`

    - [euro2020](scraping/women/euro2020)
      - `euro2020ub.csv` - `euro2020ub`
      - `euro2020vt.py` - `euro2020vt`
      - `euro2020ub.py` - `euro2020ub`
      - `euro2020bb.py` - `euro2020bb`
      - `euro2020fx.csv` - `euro2020fx`
      - `euro2020fx.py` - `euro2020fx`
      - `euro2020bb.csv` - `euro2020bb`
      - `euro2020vt.csv` - `euro2020vt`

- [EDA](EDA)

  - `EDA To-Do.ipynb` - `EDA To-Do`
  - `clean22_23mens.ipynb` - `clean22_23mens`

  - [men](EDA/men)

    - `Mens team selection.ipynb` - `Mens team selection`
    - `ph.ipynb` - `ph`

  - [women](EDA/women)

- [Combine_Data](Combine_Data)

  - [men](Combine_Data/men)

    - `encoded_sr.ipynb` - `encoded_sr`
    - `combine_iaa.ipynb` - `combine_iaa`
    - `fx_encoded.json` - `fx_encoded`
    - `combine_vt.ipynb` - `combine_vt`
    - `encoded_iaa_24.ipynb` - `encoded_iaa_24`
    - `iaa_encoded2024.csv` - `iaa_encoded2024`
    - `iaa2024.csv` - `iaa2024`
    - `fx_encoded.csv` - `fx_encoded`
    - `iaa2020.csv` - `iaa2020`
    - `sr_encoded.csv` - `sr_encoded`
    - `combine_iaa_24.ipynb` - `combine_iaa_24`
    - `vt.csv` - `vt`
    - `encoded_m_olympics_iaanames.csv` - `encoded_m_olympics_iaanames`
    - `encode_fx.ipynb` - `encode_fx`
    - `mens_data_size.ipynb` - `mens_data_size`
    - `mens2020to2012olympics_team.ipynb` - `mens2020to2012olympics_team`
    - `combine_ph.ipynb` - `combine_ph`
    - `hb.csv` - `hb`
    - `encode_hb.ipynb` - `encode_hb`
    - `encode_pb.ipynb` - `encode_pb`
    - `encoded_m_olympics_iaa.csv` - `encoded_m_olympics_iaa`
    - `encoded_iaa.ipynb` - `encoded_iaa`
    - `fx.csv` - `fx`
    - `pb.csv` - `pb`
    - `encode_ph.ipynb` - `encode_ph`
    - `vt_encoded.csv` - `vt_encoded`
    - `combine_fx.ipynb` - `combine_fx`
    - `iaa_encoded.csv` - `iaa_encoded`
    - `ph.csv` - `ph`
    - `sr.csv` - `sr`
    - `hb_encoded.csv` - `hb_encoded`
    - `pb_encoded.csv` - `pb_encoded`
    - `combine_sr.ipynb` - `combine_sr`
    - `ph_encoded.csv` - `ph_encoded`
    - `encoded_vt.ipynb` - `encoded_vt`
    - `combine_pb.ipynb` - `combine_pb`
    - `combine_hb.ipynb` - `combine_hb`

  - [women](Combine_Data/women)
    - `olympics_Women_bb.ipynb` - `olympics_Women_bb`
    - `combine_ub.ipynb` - `combine_ub`
    - `combine_iaa.ipynb` - `combine_iaa`
    - `combine_vt.ipynb` - `combine_vt`
    - `explore and encode womens ub.ipynb` - `explore and encode womens ub`
    - `iaa2024.csv` - `iaa2024`
    - `fx_encoded.csv` - `fx_encoded`
    - `iaa2020.csv` - `iaa2020`
    - `encoded_w_olympics_iaa.csv` - `encoded_w_olympics_iaa`
    - `combine_iaa24.ipynb` - `combine_iaa24`
    - `ub_w.csv` - `ub_w`
    - `vt_w.csv` - `vt_w`
    - `ub_encoded.csv` - `ub_encoded`
    - `explore amd encode womens vt.ipynb` - `explore amd encode womens vt`
    - `encoded_iaa.ipynb` - `encoded_iaa`
    - `mult_fx_w.csv` - `mult_fx_w`
    - `vt_encoded.csv` - `vt_encoded`
    - `encoded_w_olympics_iaanames.csv` - `encoded_w_olympics_iaanames`
    - `explore  and encode womens bb.ipynb` - `explore  and encode womens bb`
    - `combine_fx.ipynb` - `combine_fx`
    - `top_women.csv` - `top_women`
    - `iaa_encoded.csv` - `iaa_encoded`
    - `combine_bb.ipynb` - `combine_bb`
    - `explore and encode womens bb.ipynb` - `explore and encode womens bb`
    - `encoded_iaa24.ipynb` - `encoded_iaa24`
    - `fx_w.csv` - `fx_w`
    - `bb_encoded.csv` - `bb_encoded`
    - `combine_usa_women.ipynb` - `combine_usa_women`
    - `bb_encoded_3.csv` - `bb_encoded_3`
    - `mult_fx_encoded.csv` - `mult_fx_encoded`
    - `bb_w.csv` - `bb_w`
    - `explore and encoder womens fx.ipynb` - `explore and encoder womens fx`

- [modeling](modeling)

  - [men](modeling/men)

    - `fx.ipynb` - `fx`
    - `mens_individuals.csv` - `mens_individuals`
    - `iaa.ipynb` - `iaa`
    - `Models_combined.ipynb` - `Models_combined`
    - `sr.ipynb` - `sr`
    - `hb.ipynb` - `hb`
    - `pb.ipynb` - `pb`
    - `vt.ipynb` - `vt`
    - `ph.ipynb` - `ph`
    - `mens_Event_list.ipynb` - `mens_Event_list`

    - [Team](modeling/men/Team)
      - `Clean_Mens_apparatus_combined2016_2020.ipynb` - `Clean_Mens_apparatus_combined2016_2020`
      - `Modeling2016_2020.ipynb` - `Modeling2016_2020`
      - `Mens_apparatus_combined.csv` - `Mens_apparatus_combined`
      - `Mens_iaa_combined.csv` - `Mens_iaa_combined`

  - [women](modeling/women)
    - `fx.ipynb` - `fx`
    - `iaa.ipynb` - `iaa`
    - `tpot_pipeline.py` - `tpot_pipeline`
    - `models_combined.ipynb` - `models_combined`
    - `womens_individuals.csv` - `womens_individuals`
    - `bb.ipynb` - `bb`
    - `Women_Event_list.ipynb` - `Women_Event_list`
    - `vt.ipynb` - `vt`
    - `Uneven Bars.ipynb` - `Uneven Bars`

- [Results](Results)

  - `womens_models.csv` - `womens_models`
  - `team_models.csv` - `team_models`
  - `womens models cleaning.ipynb` - `womens models cleaning`
  - `women_models_athletes.csv` - `women_models_athletes`
  - `women_team_count.csv` - `women_team_count`
  - `women_models.csv` - `women_models`
  - `men_team.csv` - `men_team`
  - `women_team.csv` - `women_team`
  - `men_top_AA.csv` - `men_top_AA`
  - `Events Data Sizes.ipynb` - `Events Data Sizes`
  - `Final Data for Dashboard.ipynb` - `Final Data for Dashboard`
  - `men_team_count.csv` - `men_team_count`
  - `men_Team_Models_Review.ipynb` - `men_Team_Models_Review`
  - `usa_vs_comp_women.ipynb` - `usa_vs_comp_women`
  - `Women Team Models Review.ipynb` - `Women Team Models Review`
  - `USA Gymnasts Likely to Medal.ipynb` - `USA Gymnasts Likely to Medal`

- [Cleaning](Cleaning)

  - `combine_everything.ipynb` - `combine_everything`
  - `clean18worldChamp.ipynb` - `clean18worldChamp`

  - [qual_events](Cleaning/qual_events)

    - [men](Cleaning/qual_events/men)

      - `wc19bmelb_pb.csv` - `wc19bmelb_pb`
      - `wc19bmelb_fx.csv` - `wc19bmelb_fx`
      - `clean_universiade2019.ipynb` - `clean_universiade2019`
      - `winter20cup_iaa.csv` - `winter20cup_iaa`
      - `iaa2019.csv` - `iaa2019`
      - `uni2019ph.csv` - `uni2019ph`
      - `world19cup_fx.csv` - `world19cup_fx`
      - `uni2019sr.csv` - `uni2019sr`
      - `world19cup_pb.csv` - `world19cup_pb`
      - `iaa.ipynb` - `iaa`
      - `iaa2018.csv` - `iaa2018`
      - `world18championship_vt.csv` - `world18championship_vt`
      - `iaa2020.csv` - `iaa2020`
      - `wc19bmelb_hb.csv` - `wc19bmelb_hb`
      - `clean_world_championship2018.ipynb` - `clean_world_championship2018`
      - `iaa2021.csv` - `iaa2021`
      - `iaa2023.csv` - `iaa2023`
      - `world19cup_iaa.csv` - `world19cup_iaa`
      - `world19cup_hb.csv` - `world19cup_hb`
      - `iaa2022.csv` - `iaa2022`
      - `uni2019iaa.csv` - `uni2019iaa`
      - `wc20baku_sr.csv` - `wc20baku_sr`
      - `wc20baku_ph.csv` - `wc20baku_ph`
      - `wc19bmelb_vt.csv` - `wc19bmelb_vt`
      - `world18championship_hb.csv` - `world18championship_hb`
      - `clean_world_cup2019melbourne.ipynb` - `clean_world_cup2019melbourne`
      - `winter20cup_sr.csv` - `winter20cup_sr`
      - `winter20cup_ph.csv` - `winter20cup_ph`
      - `clean_winter_cup2020.ipynb` - `clean_winter_cup2020`
      - `world18championship_fx.csv` - `world18championship_fx`
      - `world18championship_pb.csv` - `world18championship_pb`
      - `clean_world_cup_2019_stuttgart.ipynb` - `clean_world_cup_2019_stuttgart`
      - `wc20baku_pb.csv` - `wc20baku_pb`
      - `uni2019vt.csv` - `uni2019vt`
      - `vt.ipynb` - `vt`
      - `wc20baku_fx.csv` - `wc20baku_fx`
      - `winter20cup_hb.csv` - `winter20cup_hb`
      - `world18championship_sr.csv` - `world18championship_sr`
      - `european_championship2019vt.csv` - `european_championship2019vt`
      - `world18championship_ph.csv` - `world18championship_ph`
      - `wc20baku_hb.csv` - `wc20baku_hb`
      - `winter20cup_pb.csv` - `winter20cup_pb`
      - `winter20cup_fx.csv` - `winter20cup_fx`
      - `world19cup_sr.csv` - `world19cup_sr`
      - `uni2019fx.csv` - `uni2019fx`
      - `world_championship2019vt_qual.csv` - `world_championship2019vt_qual`
      - `wc20baku_vt.csv` - `wc20baku_vt`
      - `uni2019pb.csv` - `uni2019pb`
      - `world19cup_ph.csv` - `world19cup_ph`
      - `world champ 2019 qual.ipynb` - `world champ 2019 qual`
      - `wc19bmelb_ph.csv` - `wc19bmelb_ph`
      - `clean_world_cup2020baku.ipynb` - `clean_world_cup2020baku`
      - `wc19bmelb_sr.csv` - `wc19bmelb_sr`
      - `winter20cup_vt.csv` - `winter20cup_vt`
      - `uni2019hb.csv` - `uni2019hb`
      - `world_championship2019vt.csv` - `world_championship2019vt`

    - [women](Cleaning/qual_events/women)
      - `clean_european_games2019fx.csv` - `clean_european_games2019fx`
      - `clean_wc19melbourne.ipynb` - `clean_wc19melbourne`
      - `euro2020ub.csv` - `euro2020ub`
      - `clean_pacific_rim2016bb.csv` - `clean_pacific_rim2016bb`
      - `clean_pan_american2014ub.csv` - `clean_pan_american2014ub`
      - `iaa23_22.ipynb` - `iaa23_22`
      - `clean_wc13cott_fx.csv` - `clean_wc13cott_fx`
      - `clean_european_championship2018.ipynb` - `clean_european_championship2018`
      - `iaa2019.csv` - `iaa2019`
      - `clean_jesolo2015.ipynb` - `clean_jesolo2015`
      - `clean_euro15champ_bb.csv` - `clean_euro15champ_bb`
      - `clean_british_championship2015fx.csv` - `clean_british_championship2015fx`
      - `iaa.ipynb` - `iaa`
      - `clean_worldcup2019melbourne_bb.csv` - `clean_worldcup2019melbourne_bb`
      - `iaa2018.csv` - `iaa2018`
      - `clean_worldcup2018jesolo_vt.csv` - `clean_worldcup2018jesolo_vt`
      - `clean_worldcup2019melbourne_vt.csv` - `clean_worldcup2019melbourne_vt`
      - `clean_worldcup2018jesolo_bb.csv` - `clean_worldcup2018jesolo_bb`
      - `clean_euro15champ_vt.csv` - `clean_euro15champ_vt`
      - `worldcup2019doha_bb.csv` - `worldcup2019doha_bb`
      - `clean_universiade2015fx.csv` - `clean_universiade2015fx`
      - `iaa2023.csv` - `iaa2023`
      - `clean_european_championship2021.ipynb` - `clean_european_championship2021`
      - `clean_wc13cottbus.ipynb` - `clean_wc13cottbus`
      - `clean_worldcup2015cott_ub.csv` - `clean_worldcup2015cott_ub`
      - `clean_brit_champ2015.ipynb` - `clean_brit_champ2015`
      - `clean_pacific_rim2016vt.csv` - `clean_pacific_rim2016vt`
      - `iaa2022.csv` - `iaa2022`
      - `clean_wc14doha_ub.csv` - `clean_wc14doha_ub`
      - `clean_worldcup2018jesolo_fx.csv` - `clean_worldcup2018jesolo_fx`
      - `clean_british_championship2015vt.csv` - `clean_british_championship2015vt`
      - `worldcup15cott_ERROR_BB.ipynb` - `worldcup15cott_ERROR_BB`
      - `clean_european_championship2021ub.csv` - `clean_european_championship2021ub`
      - `clean_universiade2015bb.csv` - `clean_universiade2015bb`
      - `clean_wc13cott_vt.csv` - `clean_wc13cott_vt`
      - `Events.ipynb` - `Events`
      - `clean_european_games2019vt.csv` - `clean_european_games2019vt`
      - `clean_jesolo2015ub.csv` - `clean_jesolo2015ub`
      - `clean_european_games2019bb.csv` - `clean_european_games2019bb`
      - `clean_pacific_rim2016fx.csv` - `clean_pacific_rim2016fx`
      - `uni2019ub.csv` - `uni2019ub`
      - `clean_worldcup2019doha_ub.csv` - `clean_worldcup2019doha_ub`
      - `clean_wc13cott_bb.csv` - `clean_wc13cott_bb`
      - `clean_pan_american2014.ipynb` - `clean_pan_american2014`
      - `clean_universiade2015vt.csv` - `clean_universiade2015vt`
      - `clean_wc14doha.ipynb` - `clean_wc14doha`
      - `clean_european_championship2018ub.csv` - `clean_european_championship2018ub`
      - `clean_euro15champ_fx.csv` - `clean_euro15champ_fx`
      - `clean_british_championship2015bb.csv` - `clean_british_championship2015bb`
      - `clean_worldcup2019melbourne_fx.csv` - `clean_worldcup2019melbourne_fx`
      - `euro2020.ipynb` - `euro2020`
      - `clean_european_championship2018vt.csv` - `clean_european_championship2018vt`
      - `clean_european_championship2021bb.csv` - `clean_european_championship2021bb`
      - `clean_universiade2015ub.csv` - `clean_universiade2015ub`
      - `clean_worldcup2015cott_fx.csv` - `clean_worldcup2015cott_fx`
      - `clean_worldcup2019doha_vt.csv` - `clean_worldcup2019doha_vt`
      - `uni2019vt.csv` - `uni2019vt`
      - `clean_wc14doha_fx.csv` - `clean_wc14doha_fx`
      - `clean_jesolo2015vt.csv` - `clean_jesolo2015vt`
      - `clean_european_games2019ub.csv` - `clean_european_games2019ub`
      - `clean_wc18jesolo.ipynb` - `clean_wc18jesolo`
      - `clean_jesolo2015bb.csv` - `clean_jesolo2015bb`
      - `clean_european_championships2015.ipynb` - `clean_european_championships2015`
      - `euro2020fx.csv` - `euro2020fx`
      - `uni2019bb.csv` - `uni2019bb`
      - `clean_worldcup2019doha_bb.csv` - `clean_worldcup2019doha_bb`
      - `clean_pan_american2014fx.csv` - `clean_pan_american2014fx`
      - `clean_wc13cott_ub.csv` - `clean_wc13cott_ub`
      - `clean_european_championship2021vt.csv` - `clean_european_championship2021vt`
      - `clean_european_championship2018bb.csv` - `clean_european_championship2018bb`
      - `clean_british_championship2015ub.csv` - `clean_british_championship2015ub`
      - `uni19.ipynb` - `uni19`
      - `clean_pacific_rim2016.ipynb` - `clean_pacific_rim2016`
      - `clean_wc14doha_vt.csv` - `clean_wc14doha_vt`
      - `clean_jesolo2015fx.csv` - `clean_jesolo2015fx`
      - `euro2020bb.csv` - `euro2020bb`
      - `uni2019fx.csv` - `uni2019fx`
      - `clean_pacific_rim2016ub.csv` - `clean_pacific_rim2016ub`
      - `clean_worldcup2015cott_vt.csv` - `clean_worldcup2015cott_vt`
      - `clean_pan_american2014bb.csv` - `clean_pan_american2014bb`
      - `clean_worldcup2019doha_fx.csv` - `clean_worldcup2019doha_fx`
      - `clean_european_championship2018fx.csv` - `clean_european_championship2018fx`
      - `clean_european_games2019.ipynb` - `clean_european_games2019`
      - `clean_euro15champ_ub.csv` - `clean_euro15champ_ub`
      - `clean_worldcup2019melbourne_ub.csv` - `clean_worldcup2019melbourne_ub`
      - `clean_worldcup2018jesolo_ub.csv` - `clean_worldcup2018jesolo_ub`
      - `clean_european_championship2021fx.csv` - `clean_european_championship2021fx`
      - `worldcup2019doha_ub.csv` - `worldcup2019doha_ub`
      - `clean_universiade2015.ipynb` - `clean_universiade2015`
      - `clean_pan_american2014vt.csv` - `clean_pan_american2014vt`
      - `worldcup2019doha.ipynb` - `worldcup2019doha`
      - `euro2020vt.csv` - `euro2020vt`
      - `clean_wc14doha_bb.csv` - `clean_wc14doha_bb`

  - [olympics](Cleaning/olympics)

    - [mens](Cleaning/olympics/mens)

      - `clean2012Olympics_Men's_artistic_team_all-around.csv` - `clean2012Olympics_Men's_artistic_team_all-around`
      - `cleaned2012team.ipynb` - `cleaned2012team`
      - `mens_sr.ipynb` - `mens_sr`
      - `cleaned2012to2020mens_medaled.csv` - `cleaned2012to2020mens_medaled`
      - `mens_hb.ipynb` - `mens_hb`
      - `mens_pb.ipynb` - `mens_pb`
      - `clean2020Olympics_Men's_artistic_team_all-around_Individuals.csv` - `clean2020Olympics_Men's_artistic_team_all-around_Individuals`
      - `mens_fx.ipynb` - `mens_fx`
      - `clean2016Olympics_Men's_artistic_team_all-around.ipynb` - `clean2016Olympics_Men's_artistic_team_all-around`
      - `clean2020Olympics_Men's_artistic_team_all-around.csv` - `clean2020Olympics_Men's_artistic_team_all-around`
      - `clean2012Olympics_Men's_artistic_team_all-around_Individuals.csv` - `clean2012Olympics_Men's_artistic_team_all-around_Individuals`
      - `clean2020Olympics_Men's_artistic_team_all-around.ipynb` - `clean2020Olympics_Men's_artistic_team_all-around`
      - `mens_vt.ipynb` - `mens_vt`
      - `clean2016Olympics_Men's_artistic_team_all-around.csv` - `clean2016Olympics_Men's_artistic_team_all-around`
      - `mens_ph.ipynb` - `mens_ph`
      - `cleaned2012to2020mens.csv` - `cleaned2012to2020mens`
      - `clean2016Olympics_Men's_artistic_team_all-around_Individuals.csv` - `clean2016Olympics_Men's_artistic_team_all-around_Individuals`

    - [womens](Cleaning/olympics/womens)
      - `clean_women12to20fx.ipynb` - `clean_women12to20fx`
      - `clean2020Olympics_women's_artistic_team_all-around_individual.csv` - `clean2020Olympics_women's_artistic_team_all-around_individual`
      - `clean_women12to20bb.ipynb` - `clean_women12to20bb`
      - `clean2016women.ipynb` - `clean2016women`
      - `clean2016Olympics_women's_artistic_team_all-around.csv` - `clean2016Olympics_women's_artistic_team_all-around`
      - `clean2012Olympics_women's_artistic_team_all-around_individual.csv` - `clean2012Olympics_women's_artistic_team_all-around_individual`
      - `clean_women12to20vt.ipynb` - `clean_women12to20vt`
      - `clean_women12to20ub.ipynb` - `clean_women12to20ub`
      - `clean2012Olympics_women's_artistic_team_all-around.csv` - `clean2012Olympics_women's_artistic_team_all-around`
      - `clean2016Olympics_women's_artistic_team_all-around_individual.csv` - `clean2016Olympics_women's_artistic_team_all-around_individual`
      - `clean2020Olympics_women's_artistic_team_all-around.csv` - `clean2020Olympics_women's_artistic_team_all-around`
      - `clean2012women.ipynb` - `clean2012women`
      - `clean2020women.ipynb` - `clean2020women`

  - [Asian2023Championships](Cleaning/Asian2023Championships)

    - `asian2023mens.ipynb` - `asian2023mens`

  - [qual2012](Cleaning/qual2012)

    - `clean2012qual_team.ipynb` - `clean2012qual_team`
    - `clean2012_team_qual.csv` - `clean2012_team_qual`

  - [top scores](Cleaning/top scores)

    - `top scores women.ipynb` - `top scores women`

  - [qual2008](Cleaning/qual2008)

    - `clean2008qual_team.ipynb` - `clean2008qual_team`
    - `clean2008qual_team.csv` - `clean2008qual_team`

  - [worldcup](Cleaning/worldcup)

    - `worldcup2020Baku_ub.ipynb` - `worldcup2020Baku_ub`
    - `worldcup2020Baku_vt.ipynb` - `worldcup2020Baku_vt`
    - `clean_worldcup2020Baku_ub.csv` - `clean_worldcup2020Baku_ub`
    - `clean_worldcup2020Baku_fx.csv` - `clean_worldcup2020Baku_fx`
    - `worldcup2020Baku_fx.ipynb` - `worldcup2020Baku_fx`
    - `worldcup2020Baku_bb.ipynb` - `worldcup2020Baku_bb`
    - `clean_worldcup2020Baku_vt.csv` - `clean_worldcup2020Baku_vt`
    - `clean_worldcup2020Baku_bb.csv` - `clean_worldcup2020Baku_bb`

  - [\*final2020](Cleaning/*final2020)

    - `indv_allrnd2020_final.ipynb` - `indv_allrnd2020_final`
    - `clean2020final_indv_uneven.csv` - `clean2020final_indv_uneven`
    - `clean2020final_indv_uneven.ipynb` - `clean2020final_indv_uneven`
    - `2020final_indiv_vaul.csv` - `2020final_indiv_vaul`
    - `clean2020final_indiv_vaul.ipynb` - `clean2020final_indiv_vaul`
    - `*clean2020final_indiv_floor*.ipynb` - `*clean2020final_indiv_floor*`
    - `clean2020final_indv_bb.csv` - `clean2020final_indv_bb`
    - `clean2020final_team_allrnd.csv` - `clean2020final_team_allrnd`
    - `clean2020final_indiv_floor.csv` - `clean2020final_indiv_floor`
    - `clean2020final_indv_bb.ipynb` - `clean2020final_indv_bb`
    - `clean2020final_team_allrnd.ipynb` - `clean2020final_team_allrnd`

  - [qual08to20](Cleaning/qual08to20)

    - `combine_quals.ipynb` - `combine_quals`
    - `clean08to12_team_qual.csv` - `clean08to12_team_qual`
    - `clean16to20_team_qual.csv` - `clean16to20_team_qual`

  - [Individuals_Results](Cleaning/Individuals_Results)

    - `blakely.csv` - `blakely`
    - `biles.ipynb` - `biles`
    - `lincoln.csv` - `lincoln`
    - `blakely.ipynb` - `blakely`
    - `biles_bb.csv` - `biles_bb`
    - `roberson.ipynb` - `roberson`
    - `chiles.csv` - `chiles`
    - `biles_vt.csv` - `biles_vt`
    - `wong.ipynb` - `wong`
    - `miller.csv` - `miller`
    - `dicello.csv` - `dicello`
    - `jones.csv` - `jones`
    - `lee.csv` - `lee`
    - `lincoln.ipynb` - `lincoln`
    - `sullivan.csv` - `sullivan`
    - `biles.csv` - `biles`
    - `Chiles.ipynb` - `Chiles`
    - `sullivan.ipynb` - `sullivan`
    - `jong.csv` - `jong`
    - `biles_fx.csv` - `biles_fx`
    - `TianaSumanasekera.ipynb` - `TianaSumanasekera`
    - `dicello.ipynb` - `dicello`
    - `wong.csv` - `wong`
    - `jong.ipynb` - `jong`
    - `roberson.csv` - `roberson`
    - `lee.ipynb` - `lee`
    - `individuals_combined.ipynb` - `individuals_combined`
    - `carey.csv` - `carey`
    - `matthews.ipynb` - `matthews`
    - `JadeCarey.ipynb` - `JadeCarey`
    - `individuals_combined.csv` - `individuals_combined`
    - `biles_ub.csv` - `biles_ub`
    - `matthews.csv` - `matthews`
    - `ShileseJones.ipynb` - `ShileseJones`
    - `ZoeMiller.ipynb` - `ZoeMiller`
    - `suman.csv` - `suman`

  - [qual2020](Cleaning/qual2020)

    - `clean_indv_qual_2020.ipynb` - `clean_indv_qual_2020`
    - `w_ind_allrnd2020clean.csv` - `w_ind_allrnd2020clean`
    - `clean2020qual_team.ipynb` - `clean2020qual_team`
    - `clean2020qual_team.csv` - `clean2020qual_team`
    - `w_ind_qual2020.csv` - `w_ind_qual2020`

  - [qual2016](Cleaning/qual2016)

    - `clean2016_team_qual.csv` - `clean2016_team_qual`
    - `clean2016_team_qual.ipynb` - `clean2016_team_qual`

  - [USOPC](Cleaning/USOPC)

    - `usopc_women_fx_october.csv` - `usopc_women_fx_october`
    - `cleaning-allyears+eda.ipynb` - `cleaning-allyears+eda`
    - `usopc_clean_women_olympic.csv` - `usopc_clean_women_olympic`
    - `usa_women_apparatus.csv` - `usa_women_apparatus`
    - `USOPC_cleaned22to23women.csv` - `USOPC_cleaned22to23women`
    - `usopc_men_nov.csv` - `usopc_men_nov`
    - `usa_women_apparatus.ipynb` - `usa_women_apparatus`
    - `usopc_women_october.csv` - `usopc_women_october`
    - `mens apparatus .ipynb` - `mens apparatus `
    - `usa_men_apparatus.ipynb` - `usa_men_apparatus`
    - `usopc_men_october.csv` - `usopc_men_october`
    - `cleaning17_21.ipynb` - `cleaning17_21`
    - `usopc_women_ub_october.csv` - `usopc_women_ub_october`
    - `usopc_women_nov.csv` - `usopc_women_nov`
    - `usopc_usa_women_olympic.csv` - `usopc_usa_women_olympic`
    - `USOPC_cleaned22to23mens.csv` - `USOPC_cleaned22to23mens`
    - `usopc_women_vt_october.csv` - `usopc_women_vt_october`
    - `sr_men.csv` - `sr_men`
    - `ph_men.csv` - `ph_men`
    - `hb_men.csv` - `hb_men`
    - `usa_men_apparatus.csv` - `usa_men_apparatus`
    - `clean22_23sep.ipynb` - `clean22_23sep`
    - `fx_men.csv` - `fx_men`
    - `vt_men.csv` - `vt_men`
    - `cleaned17to21.csv` - `cleaned17to21`
    - `pb_men.csv` - `pb_men`
    - `cleaned22to23men_women.ipynb` - `cleaned22to23men_women`
    - `october.ipynb` - `october`
    - `usopc_women_bb_october.csv` - `usopc_women_bb_october`

  - [World_Championships](Cleaning/World_Championships)

    - `ub_world_championship_w.csv` - `ub_world_championship_w`
    - `clean19worldChamp.ipynb` - `clean19worldChamp`
    - `world18champs.csv` - `world18champs`
    - `clean2023Camp.ipynb` - `clean2023Camp`
    - `vt_world_championship_w.csv` - `vt_world_championship_w`
    - `clean18worldChamp.ipynb` - `clean18worldChamp`
    - `world19champs.csv` - `world19champs`
    - `bb_world_championship_w.csv` - `bb_world_championship_w`
    - `fx_world_championship_w.csv` - `fx_world_championship_w`
    - `world_championships_combined.ipynb` - `world_championships_combined`

    - [world_champ_wiki](Cleaning/World_Championships/world_champ_wiki)
      - `wc14bb.csv` - `wc14bb`
      - `wc11fx.csv` - `wc11fx`
      - `wc19.ipynb` - `wc19`
      - `wc13fx.csv` - `wc13fx`
      - `wc18_ERROR_VT.ipynb` - `wc18_ERROR_VT`
      - `wc17fx.csv` - `wc17fx`
      - `wc_w_bb.ipynb` - `wc_w_bb`
      - `wc15fx.csv` - `wc15fx`
      - `wc14vt.csv` - `wc14vt`
      - `wc_w_iaa.ipynb` - `wc_w_iaa`
      - `wc18ub.csv` - `wc18ub`
      - `wc11_19w_ub.csv` - `wc11_19w_ub`
      - `wc14w.ipynb` - `wc14w`
      - `wc17bb.csv` - `wc17bb`
      - `wc13vt.csv` - `wc13vt`
      - `wc11vt.csv` - `wc11vt`
      - `wc15bb.csv` - `wc15bb`
      - `wc14fx.csv` - `wc14fx`
      - `wc19ub.csv` - `wc19ub`
      - `wc15vt.csv` - `wc15vt`
      - `wc11bb.csv` - `wc11bb`
      - `wc13bb.csv` - `wc13bb`
      - `wc18iaa.csv` - `wc18iaa`
      - `wc14iaa.csv` - `wc14iaa`
      - `wc17vt.csv` - `wc17vt`
      - `wc13w.ipynb` - `wc13w`
      - `wc11iaa.csv` - `wc11iaa`
      - `wc11_19w_bb.csv` - `wc11_19w_bb`
      - `wc_w_vt.ipynb` - `wc_w_vt`
      - `wc17ub.csv` - `wc17ub`
      - `wc_w_ub.ipynb` - `wc_w_ub`
      - `wc11_19w_iaa.csv` - `wc11_19w_iaa`
      - `wc15ub.csv` - `wc15ub`
      - `wc19vt.csv` - `wc19vt`
      - `wc18fx.csv` - `wc18fx`
      - `wc19bb.csv` - `wc19bb`
      - `wc11ub.csv` - `wc11ub`
      - `wc13ub.csv` - `wc13ub`
      - `wc13iaa.csv` - `wc13iaa`
      - `wc11w.ipynb` - `wc11w`
      - `wc11_19w_vt.csv` - `wc11_19w_vt`
      - `wc18vt.csv` - `wc18vt`
      - `wc14ub.csv` - `wc14ub`
      - `wc19fx.csv` - `wc19fx`
      - `wc17iaa.csv` - `wc17iaa`
      - `wc19iaa.csv` - `wc19iaa`
      - `wc15.ipynb` - `wc15`
      - `wc15iaa.csv` - `wc15iaa`
      - `wc17.ipynb` - `wc17`
      - `wc18bb.csv` - `wc18bb`

- [Data](Data)

  - [cleandata22-23](Data/cleandata22-23)

    - `encoded_m_olympics_vtnames.csv` - `encoded_m_olympics_vtnames`
    - `women_and_mens22-23CLEAN.ipynb` - `women_and_mens22-23CLEAN`
    - `encoded_w_olympics_ub.csv` - `encoded_w_olympics_ub`
    - `encoded_w_olympics_ubnames.csv` - `encoded_w_olympics_ubnames`
    - `encoded_m_olympics_sr.csv` - `encoded_m_olympics_sr`
    - `encoded_m_olympics_ph.csv` - `encoded_m_olympics_ph`
    - `women22_23.csv` - `women22_23`
    - `clean_encode.ipynb` - `clean_encode`
    - `data_2022_2023.csv` - `data_2022_2023`
    - `encoded_w_olympics_vtnames.csv` - `encoded_w_olympics_vtnames`
    - `data_2017_2021.csv` - `data_2017_2021`
    - `usa22_23.csv` - `usa22_23`
    - `encoded_m_olympics_srnames.csv` - `encoded_m_olympics_srnames`
    - `encoded_w_olympics_fx.csv` - `encoded_w_olympics_fx`
    - `encoded_m_olympics_pb.csv` - `encoded_m_olympics_pb`
    - `encoded_m_olympics_fxnames.csv` - `encoded_m_olympics_fxnames`
    - `encoded_m_olympics_fx.csv` - `encoded_m_olympics_fx`
    - `encoded_m_olympics_phnames.csv` - `encoded_m_olympics_phnames`
    - `encoded_m_olympics_hbnames.csv` - `encoded_m_olympics_hbnames`
    - `encoded_w_olympics_bbnames.csv` - `encoded_w_olympics_bbnames`
    - `encoded_m_olympics_pbnames.csv` - `encoded_m_olympics_pbnames`
    - `men22_23.csv` - `men22_23`
    - `encoded_m_olympics_hb.csv` - `encoded_m_olympics_hb`
    - `encoded_m_olympics_vt.csv` - `encoded_m_olympics_vt`
    - `usa_men22_23.csv` - `usa_men22_23`
    - `encoded_w_olympics_vt.csv` - `encoded_w_olympics_vt`
    - `encoded_w_olympics_bb.csv` - `encoded_w_olympics_bb`
    - `clean_encode_men.ipynb` - `clean_encode_men`
    - `encoded_w_olympics_fxnames.csv` - `encoded_w_olympics_fxnames`

  - [asia2023championship_men](Data/asia2023championship_men)
    - `pb23mens.csv` - `pb23mens`
    - `floor23mens.csv` - `floor23mens`
    - `vault23mens.csv` - `vault23mens`
    - `asia2023mens.py` - `asia2023mens`
    - `ph23mens.csv` - `ph23mens`
    - `hb23mens.csv` - `hb23mens`
    - `mens2023iaa.csv` - `mens2023iaa`
    - `rings23mens.csv` - `rings23mens`

- [Team_Selection](Team_Selection)

  - `final_rnd_team.ipynb` - `final_rnd_team`
  - `team_from_ind_scores.csv` - `team_from_ind_scores`
  - `Team from Individuals.ipynb` - `Team from Individuals`
  - `Metaheuristics.ipynb` - `Metaheuristics`
  - `team_from_ind.csv` - `team_from_ind`
  - `Simone Biles_data.csv` - `Simone Biles_data`

  - [images](Team_Selection/images)

    - `Screenshot 2023-11-20 at 8.04.36 AM.png` - `Screenshot 2023-11-20 at 8.04.36 AM`
    - `Screenshot 2023-11-19 at 7.14.26 PM.png` - `Screenshot 2023-11-19 at 7.14.26 PM`
    - `Screenshot 2023-11-19 at 7.12.42 PM.png` - `Screenshot 2023-11-19 at 7.12.42 PM`
    - `Screenshot 2023-11-19 at 8.03.25 PM.png` - `Screenshot 2023-11-19 at 8.03.25 PM`

  - [men](Team_Selection/men)

    - `report.log` - `report`
    - `all_usa.csv` - `all_usa`
    - `update_usa_apparatus.csv` - `update_usa_apparatus`
    - `top_men_cleaning.ipynb` - `top_men_cleaning`
    - `Metaheuristics.ipynb` - `Metaheuristics`
    - `top_men.csv` - `top_men`
    - `usa_men.csv` - `usa_men`

  - [Competition](Team_Selection/Competition)

    - `great_britain.csv` - `great_britain`
    - `top_countries.ipynb` - `top_countries`
    - `canada.csv` - `canada`
    - `Canada.ipynb` - `Canada`
    - `france.csv` - `france`
    - `top_countries.csv` - `top_countries`
    - `Great_Britian.ipynb` - `Great_Britian`
    - `brazil.csv` - `brazil`
    - `Countries.ipynb` - `Countries`
    - `Brazil.ipynb` - `Brazil`
    - `France.ipynb` - `France`
    - `china.csv` - `china`
    - `China.ipynb` - `China`

    - [Men](Team_Selection/Competition/Men)
      - `Japan.ipynb` - `Japan`
      - `germany.ipynb` - `germany`
      - `UK.ipynb` - `UK`
      - `uk.csv` - `uk`
      - `japan.csv` - `japan`
      - `Qualified teams.ipynb` - `Qualified teams`
      - `swiss.ipynb` - `swiss`
      - `usa.ipynb` - `usa`
      - `de.csv` - `de`
      - `usa.csv` - `usa`
      - `china.csv` - `china`
      - `china.ipynb` - `china`
      - `ch.csv` - `ch`
