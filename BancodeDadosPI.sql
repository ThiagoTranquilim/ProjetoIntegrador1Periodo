--------------------------------------------------------
--  Arquivo criado - segunda-feira-maio-29-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table PI
--------------------------------------------------------

  CREATE TABLE "BD240223111"."PI" 
   (	"ID" NUMBER(*,0), 
	"MP10" NUMBER(*,0), 
	"MP25" NUMBER(*,0), 
	"O3" NUMBER(*,0), 
	"CO" NUMBER(*,0), 
	"NO2" NUMBER(*,0), 
	"SO2" NUMBER(*,0)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into BD240223111.PI
SET DEFINE OFF;
Insert into BD240223111.PI (ID,MP10,MP25,O3,CO,NO2,SO2) values ('3','150','75','160','13','320','365');
Insert into BD240223111.PI (ID,MP10,MP25,O3,CO,NO2,SO2) values ('2','100','50','130','11','240','40');
Insert into BD240223111.PI (ID,MP10,MP25,O3,CO,NO2,SO2) values ('4','250','125','200','15','1130','800');
Insert into BD240223111.PI (ID,MP10,MP25,O3,CO,NO2,SO2) values ('5','251','126','201','16','1131','801');
--------------------------------------------------------
--  Constraints for Table PI
--------------------------------------------------------

  ALTER TABLE "BD240223111"."PI" MODIFY ("ID" NOT NULL ENABLE);
  ALTER TABLE "BD240223111"."PI" MODIFY ("MP10" NOT NULL ENABLE);
  ALTER TABLE "BD240223111"."PI" MODIFY ("MP25" NOT NULL ENABLE);
  ALTER TABLE "BD240223111"."PI" MODIFY ("O3" NOT NULL ENABLE);
  ALTER TABLE "BD240223111"."PI" MODIFY ("CO" NOT NULL ENABLE);
  ALTER TABLE "BD240223111"."PI" MODIFY ("NO2" NOT NULL ENABLE);
  ALTER TABLE "BD240223111"."PI" MODIFY ("SO2" NOT NULL ENABLE);
